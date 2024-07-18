
import torch
from model import MODE
import argparse
from peft import PeftModel


def set_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ori_model_dir', default="ChatGLM2-6B", type=str, help='')
    parser.add_argument('--model_dir', default="output-glm2/epoch-2-step-3900/", type=str, help='')
    parser.add_argument('--mode', default="glm2", type=str, help='')

    return parser.parse_args()


if __name__ == '__main__':
    args = set_args()
    base_model = MODE[args.mode]["model"].from_pretrained(args.ori_model_dir, torch_dtype=torch.float16)
    lora_model = PeftModel.from_pretrained(base_model, args.model_dir, torch_dtype=torch.float16)
    lora_model.to("cpu")
    model = lora_model.merge_and_unload()
    MODE[args.mode]["model"].save_pretrained(model, args.model_dir, max_shard_size="2GB")
