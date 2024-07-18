#!/bin/bash


OUTPUT=$1
ZERO_STAGE=$2
if [ "$OUTPUT" == "" ]; then
    OUTPUT=/path/to/freeze
fi
if [ "$ZERO_STAGE" == "" ]; then
    ZERO_STAGE=3
fi
mkdir -p $OUTPUT
CUDA_VISIBLE_DEVICES=0,1,2,3 deepspeed --master_port 520 train.py \
                --train_path /path/to/data \
                --model_name_or_path /path/to/model/ \
                --per_device_train_batch_size 1 \
                --max_len 1560 \
                --max_src_len 1024 \
                --learning_rate 5e-4 \
                --weight_decay 0.1 \
                --num_train_epochs 20 \
                --gradient_accumulation_steps 4 \
                --warmup_ratio 0.1 \
                --mode glm3 \
                --train_type freeze \
                --freeze_module_name "layers.27.,layers.26.layers.25.layers.24." \
                --seed 1234 \
                --ds_file /path/to/ds_zero3_no_offload.json \
                --gradient_checkpointing \
                --show_loss_step 10 \
                --output_dir $OUTPUT \
                --dataset_length 100\
                 &> $OUTPUT/training_raw_data.log

