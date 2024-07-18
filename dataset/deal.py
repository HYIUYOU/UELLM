import json
import random

# Read the raw JSON data file
with open('/path/to/data', 'r') as file:
    data = json.load(file)

# Process the "output" field in each JSON object
# Add the SLO field
for obj in data:
    obj["SLO"] = random.randint(150, 300)
    obj["output"] = len(obj["output"])
for obj in data[:20]:
    obj["SLO"] = random.randint(220, 250)
    
for obj in data[20:40]:
    obj["SLO"] = random.randint(180, 220)

for obj in data[40:60]:
    obj["SLO"] = random.randint(150, 180)

for obj in data[60:80]:
    obj["SLO"] = random.randint(100, 120)

for obj in data[80:100]:
    obj["SLO"] = random.randint(90, 100)


# Save the modified data to a new JSON file
with open('/path/to/data', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("The modified data has been saved to the data_with_slo.json file.")

