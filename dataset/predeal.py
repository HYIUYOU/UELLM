import json

# Reading raw JSON data
with open('/path/to/data', 'r', encoding='utf-8') as file:
    data = json.load(file)

#data = data[:100]
# Filter elements whose input is empty
filtered_data = [item for item in data if not item["input"]]

# Writing a new JSON file
with open('/path/to/model', 'w', encoding='utf-8') as file:
    json.dump(filtered_data, file, indent=4, ensure_ascii=False)
