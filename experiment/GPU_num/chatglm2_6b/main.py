batch_size = 5
THRESHOLD = 50
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0,1,2,3"
num_gpus=4
q = 10
import json

# Open and read JSON files
with open('/path/to/data', 'r') as file:
    data = json.load(file)

data = data[q-1]
#print(data)

from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained("chatglm2-6b", trust_remote_code=True)
from utils import load_model_on_gpus
model = load_model_on_gpus("chatglm2-6b", num_gpus=num_gpus)
#model = AutoModel.from_pretrained("chatglm2-6b", trust_remote_code=True).half().cuda()
model = model.eval()

historys = [[], []] 


import time
start = time.time()

print("q",q,data['instruction'])

print("num_gpus:",num_gpus)
response, history = model.chat(tokenizer, data['instruction'], history=[])
#response,historys = model.chat(tokenizer, data['instruction'], historys)
   
    
    
end = time.time()
print("baseline time:",end-start)  
    
print("==========================================================")    