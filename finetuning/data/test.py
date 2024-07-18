import json

# Assuming your JSON data is stored in a file called "data.json"
with open('modified_dataset_string.json', 'r') as file:
    data = json.load(file)

# Number of statistic entries
number_of_items = len(data)

# Print the number of data entries
print("Total number of data items:", number_of_items)

# Read and convert data
for item in data:
    # Convert the output field from a string to an integer
    output_as_int = int(item['output'])

    # Print the converted data
    print("Instruction:", item['instruction'])
    print("Input:", item['input'])
    print("Output (as int):", output_as_int)
    print("---")
