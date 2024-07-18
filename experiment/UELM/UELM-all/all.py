
THRESHOLD = 15000
import os
ar = 100
a = 1  # SLO coefficient
b = 0.5  # output coefficient
# Set CUDA_VISIBLE_DEVICES
os.environ["CUDA_VISIBLE_DEVICES"] = "0,1,3,4"
class query:
    def __init__(self, instruction, output,SLO):
        self.instruction = instruction
        self.output = output
        self.SLO = SLO

import json

# Open and read JSON files
with open('/path/to/data', 'r') as file:
    data = json.load(file)

data = data[:ar]
# Convert the read dictionary into a list of objects
querys = [query(d['instruction'], d['output'],d['SLO']) for d in data]

print("There are ",len(querys)," instructions in total.")

#Using Scheduling Algorithms
def groupPrograms(querys):
    # Sort prompt and its index by calculation amount
    sorted_querys = sorted(querys, key=lambda x: a * x.SLO + b *x.output)

    groups = []
   
    current_group = []
    current_max = sorted_querys[0].output
    current_min = 2049

    for q in sorted_querys:
        batch_size = 10
        if current_max < 513 and current_max > 256:
            batch_size = 10
        if current_max < 1025 and current_max > 512:
            batch_size = 10
        if current_max < 2049 and current_max > 1024:
            batch_size = 10
        
        if len(current_group)<batch_size and (q.output - current_max) * (len(current_group) + 1) * 1.2 <= THRESHOLD: # 0.1 is the estimated additional consumption in parallel
            # Add prompt to the current group
            #current_group.append(q.instruction)
            current_group.append(q)
            current_max = max(current_max, q.output)
            current_min = min(current_min, q.output)
        else:
            # The current group is finished, and a new group is started
            groups.append(current_group)
           # current_group = [q.instruction]
            current_group = [q]
            current_max = q.output

    # Add the last group
    if current_group:
        groups.append(current_group)

    return groups 



output = groupPrograms(querys)


#Output the value of each element in output. Notice that the instruction and value of each element in output (notice that it is an object) need to be output here
def printGroup(output):
    print("There are ",len(output)," groups in total.")
    print("====================================")
    for i in range(len(output)):
        print("Group ",i+1,"：","Length:",len(output[i]))
        for j in range(len(output[i])):
            print("Instructions:",output[i][j])
            #print("Calculation Amount：",output[i][j].output)
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

    #Record the current time
    import time
    start = time.time()
    print("There are ",len(output)," groups in total.")
    for i in range(len(output)):
        max_token = 0 
        historys = [[] for _ in output[i]]
        query = []
        for j in range(len(output[i])):
            max_token = max(max_token,output[i][j].output)
            query += [output[i][j].instruction]
        #print("max_token:",max_token)
        #print("query:",query)
        response,outputs,inputs = model.chat_batch(tokenizer, query, historys,max_token+50)
        end = time.time()
        t = end-start
        #print("baseline time:",t)
        for j in range(len(output[i])):
            #print("SLO:",grouped_slos[i][j])    
            if output[i][j].SLO < t:
                l += 1
        # print("Group ",i+1,"：")
        # print("Instructions:",output[i])
        # for j in range(len(output[i])):
        #     print("Instructions:",output[i][j])
            # print("Calculation Amount：",output[i][j].output)
        # print("====================================")
    end = time.time()
    print("ODBS time:",end-start)  
    print("ODBS Default Rate:",l/len(data)) 
    print("==========================================================")    


#printGroup(output)
run()


