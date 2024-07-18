import os
from typing import Dict, Tuple, Union, Optional

from torch.nn import Module
from transformers import AutoModel


def auto_configure_device_map(num_gpus: int) -> Dict[str, int]:
    # transformer.word_embeddings occupies 1 layer
    # transformer.final_layernorm and lm_head occupies 1 layer
    # transformer.layers occupies 28 layers
    # 30 layers in total, distributed to num_gpus cards
    num_trans_layers = 28
    per_gpu_layers = 30 / num_gpus

    # bugfix: In Linux, the weight passed in by calling torch.embedding is not on the same device, resulting in RuntimeError
    # In Windows, model.device will be set to transformer.word_embeddings.device
    # In Linux, model.device will be set to lm_head.device
    # When calling chat or stream_chat, input_ids will be placed on model.device
    # If transformer.word_embeddings.device and model.device are different, it will cause RuntimeError
    # Therefore, transformer.word_embeddings, transformer.final_layernorm, and lm_head are all placed on the first card here
    # This file comes from https://github.com/THUDM/ChatGLM-6B/blob/main/utils.py
    # Only a few changes are made here to support ChatGLM2
    device_map = {
        'transformer.embedding.word_embeddings': 0,
        'transformer.encoder.final_layernorm': 0,
        'transformer.output_layer': 0,
        'transformer.rotary_pos_emb': 0,
        'lm_head': 0
    }

    used = 2
    gpu_target = 0
    for i in range(num_trans_layers):
        if used >= per_gpu_layers:
            gpu_target += 1
            used = 0
        assert gpu_target < num_gpus
        device_map[f'transformer.encoder.layers.{i}'] = gpu_target
        used += 1

    return device_map


def load_model_on_gpus(checkpoint_path: Union[str, os.PathLike], num_gpus: int = 2,
                       device_map: Optional[Dict[str, int]] = None, **kwargs) -> Module:
    if num_gpus < 2 and device_map is None:
        model = AutoModel.from_pretrained(checkpoint_path, trust_remote_code=True, **kwargs).half().cuda()
    else:
        from accelerate import dispatch_model

        model = AutoModel.from_pretrained(checkpoint_path, trust_remote_code=True, **kwargs).half()

        if device_map is None:
            device_map = auto_configure_device_map(num_gpus)

        model = dispatch_model(model, device_map=device_map)

    return model
