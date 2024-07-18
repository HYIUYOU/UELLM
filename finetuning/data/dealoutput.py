# Example Python code to extract numbers from the given string format

import re

# Simulating the input as a long string
input_string1 = """
returning input_ids
input ids shape:  torch.Size([1, 246])
returning input_ids
input ids shape:  torch.Size([1, 251])
returning input_ids
input ids shape:  torch.Size([1, 226])
returning input_ids
input ids shape:  torch.Size([1, 207])
returning input_ids
input ids shape:  torch.Size([1, 393])
returning input_ids
input ids shape:  torch.Size([1, 156])
returning input_ids
input ids shape:  torch.Size([1, 298])
returning input_ids
input ids shape:  torch.Size([1, 160])
returning input_ids
input ids shape:  torch.Size([1, 53])
returning input_ids
input ids shape:  torch.Size([1, 294])
returning input_ids
input ids shape:  torch.Size([1, 213])
returning input_ids
input ids shape:  torch.Size([1, 202])
returning input_ids
input ids shape:  torch.Size([1, 105])
returning input_ids
input ids shape:  torch.Size([1, 354])
returning input_ids
input ids shape:  torch.Size([1, 25])
returning input_ids
input ids shape:  torch.Size([1, 85])
returning input_ids
input ids shape:  torch.Size([1, 208])
returning input_ids
input ids shape:  torch.Size([1, 178])
returning input_ids
input ids shape:  torch.Size([1, 268])
returning input_ids
input ids shape:  torch.Size([1, 226])
returning input_ids
input ids shape:  torch.Size([1, 80])
returning input_ids
input ids shape:  torch.Size([1, 168])
returning input_ids
input ids shape:  torch.Size([1, 196])
returning input_ids
input ids shape:  torch.Size([1, 59])
returning input_ids
input ids shape:  torch.Size([1, 135])
returning input_ids
input ids shape:  torch.Size([1, 169])
returning input_ids
input ids shape:  torch.Size([1, 524])
returning input_ids
input ids shape:  torch.Size([1, 89])
returning input_ids
input ids shape:  torch.Size([1, 131])
returning input_ids
input ids shape:  torch.Size([1, 204])
returning input_ids
input ids shape:  torch.Size([1, 39])
returning input_ids
input ids shape:  torch.Size([1, 48])
returning input_ids
input ids shape:  torch.Size([1, 333])
returning input_ids
input ids shape:  torch.Size([1, 215])
returning input_ids
input ids shape:  torch.Size([1, 108])
returning input_ids
input ids shape:  torch.Size([1, 149])
returning input_ids
input ids shape:  torch.Size([1, 18])
returning input_ids
input ids shape:  torch.Size([1, 171])
returning input_ids
input ids shape:  torch.Size([1, 41])
returning input_ids
input ids shape:  torch.Size([1, 50])
returning input_ids
input ids shape:  torch.Size([1, 104])
returning input_ids
input ids shape:  torch.Size([1, 538])
returning input_ids
input ids shape:  torch.Size([1, 74])
returning input_ids
input ids shape:  torch.Size([1, 152])
returning input_ids
input ids shape:  torch.Size([1, 443])
returning input_ids
input ids shape:  torch.Size([1, 131])
returning input_ids
input ids shape:  torch.Size([1, 400])
returning input_ids
input ids shape:  torch.Size([1, 163])
returning input_ids
input ids shape:  torch.Size([1, 286])
returning input_ids
input ids shape:  torch.Size([1, 141])
returning input_ids
input ids shape:  torch.Size([1, 254])
returning input_ids
input ids shape:  torch.Size([1, 131])
returning input_ids
input ids shape:  torch.Size([1, 264])
returning input_ids
input ids shape:  torch.Size([1, 344])
returning input_ids
input ids shape:  torch.Size([1, 188])
returning input_ids
input ids shape:  torch.Size([1, 81])
returning input_ids
input ids shape:  torch.Size([1, 67])
returning input_ids
input ids shape:  torch.Size([1, 58])
returning input_ids
input ids shape:  torch.Size([1, 90])
returning input_ids
input ids shape:  torch.Size([1, 283])
returning input_ids
input ids shape:  torch.Size([1, 179])
returning input_ids
input ids shape:  torch.Size([1, 182])
returning input_ids
input ids shape:  torch.Size([1, 199])
returning input_ids
input ids shape:  torch.Size([1, 525])
returning input_ids
input ids shape:  torch.Size([1, 221])
returning input_ids
input ids shape:  torch.Size([1, 102])
returning input_ids
input ids shape:  torch.Size([1, 39])
returning input_ids
input ids shape:  torch.Size([1, 170])
returning input_ids
input ids shape:  torch.Size([1, 199])
returning input_ids
input ids shape:  torch.Size([1, 123])
returning input_ids
input ids shape:  torch.Size([1, 164])
returning input_ids
input ids shape:  torch.Size([1, 273])
returning input_ids
input ids shape:  torch.Size([1, 436])
returning input_ids
input ids shape:  torch.Size([1, 23])
returning input_ids
input ids shape:  torch.Size([1, 11])
returning input_ids
input ids shape:  torch.Size([1, 47])
returning input_ids
input ids shape:  torch.Size([1, 58])
returning input_ids
input ids shape:  torch.Size([1, 639])
returning input_ids
input ids shape:  torch.Size([1, 323])
returning input_ids
input ids shape:  torch.Size([1, 97])
returning input_ids
input ids shape:  torch.Size([1, 132])
returning input_ids
input ids shape:  torch.Size([1, 305])
returning input_ids
input ids shape:  torch.Size([1, 50])
returning input_ids
input ids shape:  torch.Size([1, 294])
returning input_ids
input ids shape:  torch.Size([1, 87])
returning input_ids
input ids shape:  torch.Size([1, 148])
returning input_ids
input ids shape:  torch.Size([1, 109])
returning input_ids
input ids shape:  torch.Size([1, 250])
returning input_ids
input ids shape:  torch.Size([1, 316])
returning input_ids
input ids shape:  torch.Size([1, 198])
returning input_ids
input ids shape:  torch.Size([1, 169])
returning input_ids
input ids shape:  torch.Size([1, 182])
returning input_ids
input ids shape:  torch.Size([1, 246])
returning input_ids
input ids shape:  torch.Size([1, 252])
returning input_ids
input ids shape:  torch.Size([1, 247])
returning input_ids
input ids shape:  torch.Size([1, 233])
returning input_ids
input ids shape:  torch.Size([1, 335])
returning input_ids
input ids shape:  torch.Size([1, 71])
returning input_ids
input ids shape:  torch.Size([1, 194])
returning input_ids
input ids shape:  torch.Size([1, 273])
"""



input_string = input_string1    
# Use regular expression to find all occurrences of the pattern describing the shape
matches = re.findall(r"torch\.Size\(\[1, (\d+)\]\)", input_string)

# Convert found strings to integers
extracted_numbers = [int(match) for match in matches]
print(extracted_numbers)

def tojson(extracted_numbers):
    import json

    # Set the path to the JSON file
    input_file_path = '/path/to/data'  # Path to the input file
    output_file_path = '/path/to/data'  # Path to the output file

    # Reading JSON Files
    with open(input_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)  # Loading JSON data

    # Iterate over the data and update the 'output' field
    for i in range(len(data)):
        # Calculate the number of characters in the original output field
        output_length = extracted_numbers[i]
        # Replace the output field with its length
        data[i]['output'] = output_length

    # 将更新后的数据写回到新的 JSON 文件
    with open(output_file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)  # Convert Python objects to JSON format and write to a file