
THRESHOLD = 15000
import os
batch_size_l = [10,10,10,10,8,6]
ar = 200
# Set CUDA_VISIBLE_DEVICES
os.environ["CUDA_VISIBLE_DEVICES"] = "0,1,3,4"
class query:
    def __init__(self, instruction, value,SLO):
        self.instruction = instruction
        self.value = value
        self.SLO = SLO

import json

# Open and read JSON file
with open('/path/to/data', 'r') as file:
    data = json.load(file)

data = data[:ar]
# Convert the read dictionary into a list of objects
querys = [query(d['instruction'], d['output'],d['SLO']) for d in data]


#Using Scheduling Algorithms
def groupPrograms(querys):
    # Sort prompt and its index by calculation amount
    sorted_querys = sorted(querys, key=lambda x: x.SLO)

    groups = []
   
    current_group = []
    current_max = sorted_querys[0].SLO
    current_min = 2049
    
    for q in sorted_querys:
        batch_size = batch_size_l[0]
        # if current_max < 100 and current_max > 90:
        #     batch_size = batch_size_l[1]
        # if current_max < 120 and current_max > 99:
        #     batch_size = batch_size_l[2]
        # if current_max < 180 and current_max > 119:
        #     batch_size = batch_size_l[3]
        # if current_max < 220 and current_max > 179:
        #     batch_size = batch_size_l[4]
        # if current_max < 250 and current_max > 219:
        #     batch_size = batch_size_l[5]
        
        #and (q.SLO - current_max) * (len(current_group) + 1) * 1.2 <= THRESHOLD
        if len(current_group)<batch_size and (q.SLO - current_max) * (len(current_group) + 1) * 1.2 <= THRESHOLD : # 0.1 is the estimated additional consumption in parallel
            # Add prompt to the current group
            #current_group.append(q.instruction)
            current_group.append(q)
            current_max = max(current_max, q.SLO)
            current_min = min(current_min, q.SLO)
        else:
            # The current group is finished, and a new group is started
            groups.append(current_group)
           # current_group = [q.instruction]
            current_group = [q]
            current_max = q.SLO

    # Add the last group
    if current_group:
        groups.append(current_group)

    return groups 



output = groupPrograms(querys)

#Output all SLOs in output
print("There are ",len(output)," groups in total.")
print("====================================")
for i in range(len(output)):
        print("Group ",i+1," :","Length:",len(output[i]))
        for j in range(len(output[i])):
            print("Instruction SLO:",output[i][j].SLO)

# Output the value of each element in output. 
# Notice that the instruction and value of each element in output (notice that it is an object) need to be output.
def printGroup(output):
    print("There are ",len(output)," groups in total.")
    print("====================================")
    for i in range(len(output)):
        print("Group ",i+1," :","Length:",len(output[i]))
        for j in range(len(output[i])):
            print("Instructions:",output[i][j])
            #print("Calculation Amount:",output[i][j].value)
        print("====================================")




def run():
    l = 0
    from transformers import AutoTokenizer, AutoModel
    tokenizer = AutoTokenizer.from_pretrained("/path/to/model", trust_remote_code=True)
    from utils import load_model_on_gpus
    model = load_model_on_gpus("/path/to/model", num_gpus=1)
    #model = AutoModel.from_pretrained("chatglm2-6b", trust_remote_code=True).half().cuda()
    model = model.eval()

    historys = [[], []] 

    # Record current time
    import time
    start = time.time()
    print("There are ",len(output),"groups in total.")
    for i in range(len(output)):
        historys = [[] for _ in output[i]]
        query = []
        max_length = []
        for j in range(len(output[i])):
            query += [output[i][j].instruction]
            max_length += [output[i][j].value]
       # print("query:",query)
        response,outputs,inputs = model.chat_batch(tokenizer, query, historys,max(max_length))
        end = time.time()
        t = end-start
        #print("baseline time:",t)
        for j in range(len(output[i])):
            #print("SLO:",grouped_slos[i][j])    
            if output[i][j].SLO < t:
                l += 1
        # print("Group ",i+1," :")
        # print("Instruction: ",output[i])
        # for j in range(len(output[i])):
        #     print(Instructions:",output[i][j])
            # print("Calculation Amount:",output[i][j].value)
        # print("====================================")
    end = time.time()
    print("ODBS time:",end-start)  
    print("ODBS Default Rate:",l/len(data)) 
    print("==========================================================")    


#printGroup(output)
run()



