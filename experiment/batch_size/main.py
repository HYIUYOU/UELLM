THRESHOLD = 50
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0,1,2,3"
num_gpus=4
batch_size = 30
import json

class query:
    def __init__(self, instruction, value):
        self.instruction = instruction
        self.value = value
# Open and read the JSON file
with open('/path/to/data', 'r') as file:
    data = json.load(file)

data = data[:batch_size]
#print(data)

from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained("/path/to/model", trust_remote_code=True)
from utils import load_model_on_gpus
model = load_model_on_gpus("/path/to/model", num_gpus=num_gpus)
#model = AutoModel.from_pretrained("chatglm2-6b", trust_remote_code=True).half().cuda()
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