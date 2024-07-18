batch_size = 1
THRESHOLD = 50
ar = 250
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0,1,2,3"

class query:
    def __init__(self, instruction, value,SLO):
        self.instruction = instruction
        self.value = value
        self.SLO = SLO

import json

# Open and read JSON files
with open('/path/to/data', 'r') as file:
    data = json.load(file)

data = data[:ar]
# print(data)
# Convert the read dictionary into a list of Person objects
querys = [query(d['instruction'], d['output'],d['SLO']) for d in data]

#querys = sorted(querys, key=lambda x: x.value)


from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained("/path/to/model", trust_remote_code=True)
from utils import load_model_on_gpus
model = load_model_on_gpus("/path/to/model", num_gpus=1)
#model = AutoModel.from_pretrained("chatglm2-6b", trust_remote_code=True).half().cuda()
model = model.eval()

historys = [[], []] 


# No scheduling algorithm is used

# Extract the instruction of each Query object and combine them into a small list
grouped_instructions = [ [q.instruction for q in querys[i:i+batch_size]] for i in range(0, len(querys), batch_size) ]
# Extract the SLO of each Query object and combine them into a small list
grouped_slos = [ [q.SLO for q in querys[i:i+batch_size]] for i in range(0, len(querys), batch_size) ]
# Record the current time
import time
start = time.time()
l = 0
for i in range(len(grouped_instructions)):
    historys = [[] for _ in grouped_instructions[i]]
    response,outputs,inputs = model.chat_batch(tokenizer, grouped_instructions[i], historys)
    end = time.time()
    t = end-start
    #print("baseline time:",t)
    for j in range(len(grouped_slos[i])):
        #print("SLO:",grouped_slos[i][j])    
        if grouped_slos[i][j] < t:
            l += 1
            
        
    
    #print(response)
    
    
end = time.time()
t = end-start
print("baseline time:",t)  
   
print("baseline Default Rate:",l/len(data))
print("==========================================================")    