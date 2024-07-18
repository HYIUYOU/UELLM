
THRESHOLD = 50
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0,1,2,3"
num_gpus=4
batch_size = 5
import json

# 5+28 = 33
# 
device_map1 = {'transformer.embedding.word_embeddings': 0, #1
              'transformer.encoder.final_layernorm': 0, #2
              'transformer.output_layer': 0, #3
              'transformer.rotary_pos_emb': 0,#4
              'lm_head': 0, #5
              'transformer.encoder.layers.0': 0,#6
              'transformer.encoder.layers.1': 0, #7
              'transformer.encoder.layers.2': 0, #8
              'transformer.encoder.layers.3': 0, #9
              'transformer.encoder.layers.4': 0,  #10
              'transformer.encoder.layers.5': 0, #11
              'transformer.encoder.layers.6': 0, #12
              'transformer.encoder.layers.7': 0, #13
              'transformer.encoder.layers.8': 0, #14
              'transformer.encoder.layers.9': 0, #15
              'transformer.encoder.layers.10': 0,#16
              'transformer.encoder.layers.11': 0,#17
              'transformer.encoder.layers.12': 0,#18
              'transformer.encoder.layers.13': 0,#19
              'transformer.encoder.layers.14': 0,#20
              'transformer.encoder.layers.15': 0,#21
              'transformer.encoder.layers.16': 0,#22
              'transformer.encoder.layers.17': 0,#23
              'transformer.encoder.layers.18': 0,#24
              'transformer.encoder.layers.19': 0,#25
              'transformer.encoder.layers.20': 0,#26
              'transformer.encoder.layers.21': 0,#27
              'transformer.encoder.layers.22': 0,#28
              'transformer.encoder.layers.23': 0,#29
              'transformer.encoder.layers.24': 0,#30
              'transformer.encoder.layers.25': 0,#31
              'transformer.encoder.layers.26': 0,#32
              'transformer.encoder.layers.27': 0 #33
              }

device_map2 = {'transformer.embedding.word_embeddings': 0, 
              'transformer.encoder.final_layernorm':0, 
              'transformer.output_layer': 0, 
              'transformer.rotary_pos_emb': 0,
              'lm_head': 0, 
              'transformer.encoder.layers.0': 1,
              'transformer.encoder.layers.1': 0, 
              'transformer.encoder.layers.2': 1, 
              'transformer.encoder.layers.3': 0, 
              'transformer.encoder.layers.4': 1, 
              'transformer.encoder.layers.5': 0, 
              'transformer.encoder.layers.6': 1, 
              'transformer.encoder.layers.7': 0, 
              'transformer.encoder.layers.8': 1, 
              'transformer.encoder.layers.9': 0, 
              'transformer.encoder.layers.10': 1,
              'transformer.encoder.layers.11': 0,
              'transformer.encoder.layers.12': 1,
              'transformer.encoder.layers.13': 0,
              'transformer.encoder.layers.14': 1,
              'transformer.encoder.layers.15': 0,
              'transformer.encoder.layers.16': 1,
              'transformer.encoder.layers.17': 0,
              'transformer.encoder.layers.18': 1,
              'transformer.encoder.layers.19': 0,
              'transformer.encoder.layers.20': 1,
              'transformer.encoder.layers.21': 0,
              'transformer.encoder.layers.22': 1,
              'transformer.encoder.layers.23': 0,
              'transformer.encoder.layers.24': 1,
              'transformer.encoder.layers.25': 0,
              'transformer.encoder.layers.26': 1,
              'transformer.encoder.layers.27': 0
              }


class query:
    def __init__(self, instruction, value):
        self.instruction = instruction
        self.value = value
# Open and read the JSON file
with open('/path/to/data', 'r') as file:
    data = json.load(file)

data = data[batch_size-1:batch_size]
#print(data)

from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained("/path/to/model", trust_remote_code=True)
from utils import load_model_on_gpus

# model = load_model_on_gpus("/path/to/model", num_gpus=num_gpus)


model = load_model_on_gpus("/path/to/model", num_gpus=num_gpus,device_map=device_map1)
#model = AutoModel.from_pretrained("chatglm2-6b", trust_remote_code=True).half().cuda()

#print("model:",model)
model = model.eval()

historys = [[], []] 


import time


# print("q",q,data['instruction'])

print("num_gpus:",num_gpus)

querys = [query(d['instruction'], d['output']) for d in data]

print("len(querys):",len(querys))

# Extract the instruction of each Query object and combine them into a small list
grouped_instructions = [d['instruction'] for d in data]

print("len(grouped_instructions):",len(grouped_instructions))
start = time.time()

historys = [[] for _ in grouped_instructions]
response,outputs,inputs = model.chat_batch(tokenizer, grouped_instructions, historys)
#response, history = model.chat(tokenizer, data['instruction'], history=[])
#response,historys = model.chat(tokenizer, data['instruction'], historys)
   
    
    
end = time.time()
print("baseline time:",end-start)  
    
print("==========================================================")    