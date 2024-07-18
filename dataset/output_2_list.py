# Example Python code to extract numbers from the given string format

import re

def deal(input_string):
    # Use regular expression to find all occurrences of the pattern describing the shape
    matches = re.findall(r"torch\.Size\(\[1, (\d+)\]\)", input_string)

    # Convert found strings to integers
    extracted_numbers = [int(match) for match in matches]
    return extracted_numbers


def tojson(extracted_numbers):
    import json

    # Set the path to the JSON file
    input_file_path = '/path/to/data'  # Path to the input file
    output_file_path = '/path/to/data'  # Path to the output file

    # Reading JSON file
    with open(input_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)  # Loading JSON data

    # Iterate over the data and update the 'output' field
    for i in range(len(data)):
        # Calculate the number of characters in the original output field
        output_length = extracted_numbers[i]
        # Replace the output field with its length
        data[i]['output'] = output_length

    # Write the updated data back to a new JSON file
    with open(output_file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)  # Convert Python objects to JSON format and write to a file
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

input_string2 = """
returning input_ids
input ids shape:  torch.Size([1, 281])
returning input_ids
input ids shape:  torch.Size([1, 226])
returning input_ids
input ids shape:  torch.Size([1, 148])
returning input_ids
input ids shape:  torch.Size([1, 170])
returning input_ids
input ids shape:  torch.Size([1, 316])
returning input_ids
input ids shape:  torch.Size([1, 428])
returning input_ids
input ids shape:  torch.Size([1, 158])
returning input_ids
input ids shape:  torch.Size([1, 745])
returning input_ids
input ids shape:  torch.Size([1, 180])
returning input_ids
input ids shape:  torch.Size([1, 376])
returning input_ids
input ids shape:  torch.Size([1, 208])
returning input_ids
input ids shape:  torch.Size([1, 126])
returning input_ids
input ids shape:  torch.Size([1, 201])
returning input_ids
input ids shape:  torch.Size([1, 429])
returning input_ids
input ids shape:  torch.Size([1, 30])
returning input_ids
input ids shape:  torch.Size([1, 375])
returning input_ids
input ids shape:  torch.Size([1, 191])
returning input_ids
input ids shape:  torch.Size([1, 344])
returning input_ids
input ids shape:  torch.Size([1, 57])
returning input_ids
input ids shape:  torch.Size([1, 261])
returning input_ids
input ids shape:  torch.Size([1, 104])
returning input_ids
input ids shape:  torch.Size([1, 163])
returning input_ids
input ids shape:  torch.Size([1, 165])
returning input_ids
input ids shape:  torch.Size([1, 92])
returning input_ids
input ids shape:  torch.Size([1, 171])
returning input_ids
input ids shape:  torch.Size([1, 178])
returning input_ids
input ids shape:  torch.Size([1, 159])
returning input_ids
input ids shape:  torch.Size([1, 76])
returning input_ids
input ids shape:  torch.Size([1, 76])
returning input_ids
input ids shape:  torch.Size([1, 34])
returning input_ids
input ids shape:  torch.Size([1, 71])
returning input_ids
input ids shape:  torch.Size([1, 48])
returning input_ids
input ids shape:  torch.Size([1, 318])
returning input_ids
input ids shape:  torch.Size([1, 214])
returning input_ids
input ids shape:  torch.Size([1, 104])
returning input_ids
input ids shape:  torch.Size([1, 230])
returning input_ids
input ids shape:  torch.Size([1, 18])
returning input_ids
input ids shape:  torch.Size([1, 262])
returning input_ids
input ids shape:  torch.Size([1, 102])
returning input_ids
input ids shape:  torch.Size([1, 49])
returning input_ids
input ids shape:  torch.Size([1, 114])
returning input_ids
input ids shape:  torch.Size([1, 531])
returning input_ids
input ids shape:  torch.Size([1, 32])
returning input_ids
input ids shape:  torch.Size([1, 110])
returning input_ids
input ids shape:  torch.Size([1, 168])
returning input_ids
input ids shape:  torch.Size([1, 151])
returning input_ids
input ids shape:  torch.Size([1, 232])
returning input_ids
input ids shape:  torch.Size([1, 50])
returning input_ids
input ids shape:  torch.Size([1, 313])
returning input_ids
input ids shape:  torch.Size([1, 75])
returning input_ids
input ids shape:  torch.Size([1, 293])
returning input_ids
input ids shape:  torch.Size([1, 122])
returning input_ids
input ids shape:  torch.Size([1, 159])
returning input_ids
input ids shape:  torch.Size([1, 253])
returning input_ids
input ids shape:  torch.Size([1, 176])
returning input_ids
input ids shape:  torch.Size([1, 228])
returning input_ids
input ids shape:  torch.Size([1, 97])
returning input_ids
input ids shape:  torch.Size([1, 226])
returning input_ids
input ids shape:  torch.Size([1, 395])
returning input_ids
input ids shape:  torch.Size([1, 416])
returning input_ids
input ids shape:  torch.Size([1, 197])
returning input_ids
input ids shape:  torch.Size([1, 206])
returning input_ids
input ids shape:  torch.Size([1, 147])
returning input_ids
input ids shape:  torch.Size([1, 348])
returning input_ids
input ids shape:  torch.Size([1, 301])
returning input_ids
input ids shape:  torch.Size([1, 441])
returning input_ids
input ids shape:  torch.Size([1, 83])
returning input_ids
input ids shape:  torch.Size([1, 285])
returning input_ids
input ids shape:  torch.Size([1, 178])
returning input_ids
input ids shape:  torch.Size([1, 111])
returning input_ids
input ids shape:  torch.Size([1, 143])
returning input_ids
input ids shape:  torch.Size([1, 331])
returning input_ids
input ids shape:  torch.Size([1, 357])
returning input_ids
input ids shape:  torch.Size([1, 45])
returning input_ids
input ids shape:  torch.Size([1, 21])
returning input_ids
input ids shape:  torch.Size([1, 73])
returning input_ids
input ids shape:  torch.Size([1, 263])
returning input_ids
input ids shape:  torch.Size([1, 428])
returning input_ids
input ids shape:  torch.Size([1, 335])
returning input_ids
input ids shape:  torch.Size([1, 84])
returning input_ids
input ids shape:  torch.Size([1, 133])
returning input_ids
input ids shape:  torch.Size([1, 208])
returning input_ids
input ids shape:  torch.Size([1, 105])
returning input_ids
input ids shape:  torch.Size([1, 251])
returning input_ids
input ids shape:  torch.Size([1, 102])
returning input_ids
input ids shape:  torch.Size([1, 232])
returning input_ids
input ids shape:  torch.Size([1, 272])
returning input_ids
input ids shape:  torch.Size([1, 256])
returning input_ids
input ids shape:  torch.Size([1, 255])
returning input_ids
input ids shape:  torch.Size([1, 142])
returning input_ids
input ids shape:  torch.Size([1, 215])
returning input_ids
input ids shape:  torch.Size([1, 235])
returning input_ids
input ids shape:  torch.Size([1, 333])
returning input_ids
input ids shape:  torch.Size([1, 190])
returning input_ids
input ids shape:  torch.Size([1, 235])
returning input_ids
input ids shape:  torch.Size([1, 385])
returning input_ids
input ids shape:  torch.Size([1, 253])
returning input_ids
input ids shape:  torch.Size([1, 77])
returning input_ids
input ids shape:  torch.Size([1, 132])
returning input_ids
input ids shape:  torch.Size([1, 211])
"""

input_string3 = """
returning input_ids
input ids shape:  torch.Size([1, 242])
returning input_ids
input ids shape:  torch.Size([1, 235])
returning input_ids
input ids shape:  torch.Size([1, 260])
returning input_ids
input ids shape:  torch.Size([1, 126])
returning input_ids
input ids shape:  torch.Size([1, 1359])
returning input_ids
input ids shape:  torch.Size([1, 244])
returning input_ids
input ids shape:  torch.Size([1, 284])
returning input_ids
input ids shape:  torch.Size([1, 250])
returning input_ids
input ids shape:  torch.Size([1, 36])
returning input_ids
input ids shape:  torch.Size([1, 453])
returning input_ids
input ids shape:  torch.Size([1, 142])
returning input_ids
input ids shape:  torch.Size([1, 128])
returning input_ids
input ids shape:  torch.Size([1, 263])
returning input_ids
input ids shape:  torch.Size([1, 282])
returning input_ids
input ids shape:  torch.Size([1, 366])
returning input_ids
input ids shape:  torch.Size([1, 298])
returning input_ids
input ids shape:  torch.Size([1, 67])
returning input_ids
input ids shape:  torch.Size([1, 362])
returning input_ids
input ids shape:  torch.Size([1, 192])
returning input_ids
input ids shape:  torch.Size([1, 163])
returning input_ids
input ids shape:  torch.Size([1, 113])
returning input_ids
input ids shape:  torch.Size([1, 114])
returning input_ids
input ids shape:  torch.Size([1, 213])
returning input_ids
input ids shape:  torch.Size([1, 112])
returning input_ids
input ids shape:  torch.Size([1, 192])
returning input_ids
input ids shape:  torch.Size([1, 130])
returning input_ids
input ids shape:  torch.Size([1, 365])
returning input_ids
input ids shape:  torch.Size([1, 98])
returning input_ids
input ids shape:  torch.Size([1, 115])
returning input_ids
input ids shape:  torch.Size([1, 174])
returning input_ids
input ids shape:  torch.Size([1, 121])
returning input_ids
input ids shape:  torch.Size([1, 58])
returning input_ids
input ids shape:  torch.Size([1, 262])
returning input_ids
input ids shape:  torch.Size([1, 195])
returning input_ids
input ids shape:  torch.Size([1, 106])
returning input_ids
input ids shape:  torch.Size([1, 68])
returning input_ids
input ids shape:  torch.Size([1, 35])
returning input_ids
input ids shape:  torch.Size([1, 230])
returning input_ids
input ids shape:  torch.Size([1, 182])
returning input_ids
input ids shape:  torch.Size([1, 53])
returning input_ids
input ids shape:  torch.Size([1, 32])
returning input_ids
input ids shape:  torch.Size([1, 696])
returning input_ids
input ids shape:  torch.Size([1, 40])
returning input_ids
input ids shape:  torch.Size([1, 54])
returning input_ids
input ids shape:  torch.Size([1, 338])
returning input_ids
input ids shape:  torch.Size([1, 233])
returning input_ids
input ids shape:  torch.Size([1, 245])
returning input_ids
input ids shape:  torch.Size([1, 213])
returning input_ids
input ids shape:  torch.Size([1, 159])
returning input_ids
input ids shape:  torch.Size([1, 174])
returning input_ids
input ids shape:  torch.Size([1, 261])
returning input_ids
input ids shape:  torch.Size([1, 81])
returning input_ids
input ids shape:  torch.Size([1, 57])
returning input_ids
input ids shape:  torch.Size([1, 347])
returning input_ids
input ids shape:  torch.Size([1, 305])
returning input_ids
input ids shape:  torch.Size([1, 92])
returning input_ids
input ids shape:  torch.Size([1, 65])
returning input_ids
input ids shape:  torch.Size([1, 81])
returning input_ids
input ids shape:  torch.Size([1, 340])
returning input_ids
input ids shape:  torch.Size([1, 352])
returning input_ids
input ids shape:  torch.Size([1, 331])
returning input_ids
input ids shape:  torch.Size([1, 200])
returning input_ids
input ids shape:  torch.Size([1, 265])
returning input_ids
input ids shape:  torch.Size([1, 263])
returning input_ids
input ids shape:  torch.Size([1, 276])
returning input_ids
input ids shape:  torch.Size([1, 77])
returning input_ids
input ids shape:  torch.Size([1, 145])
returning input_ids
input ids shape:  torch.Size([1, 324])
returning input_ids
input ids shape:  torch.Size([1, 101])
returning input_ids
input ids shape:  torch.Size([1, 120])
returning input_ids
input ids shape:  torch.Size([1, 156])
returning input_ids
input ids shape:  torch.Size([1, 275])
returning input_ids
input ids shape:  torch.Size([1, 387])
returning input_ids
input ids shape:  torch.Size([1, 80])
returning input_ids
input ids shape:  torch.Size([1, 19])
returning input_ids
input ids shape:  torch.Size([1, 78])
returning input_ids
input ids shape:  torch.Size([1, 59])
returning input_ids
input ids shape:  torch.Size([1, 395])
returning input_ids
input ids shape:  torch.Size([1, 187])
returning input_ids
input ids shape:  torch.Size([1, 85])
returning input_ids
input ids shape:  torch.Size([1, 158])
returning input_ids
input ids shape:  torch.Size([1, 294])
returning input_ids
input ids shape:  torch.Size([1, 156])
returning input_ids
input ids shape:  torch.Size([1, 214])
returning input_ids
input ids shape:  torch.Size([1, 86])
returning input_ids
input ids shape:  torch.Size([1, 128])
returning input_ids
input ids shape:  torch.Size([1, 159])
returning input_ids
input ids shape:  torch.Size([1, 235])
returning input_ids
input ids shape:  torch.Size([1, 201])
returning input_ids
input ids shape:  torch.Size([1, 53])
returning input_ids
input ids shape:  torch.Size([1, 216])
returning input_ids
input ids shape:  torch.Size([1, 229])
returning input_ids
input ids shape:  torch.Size([1, 277])
returning input_ids
input ids shape:  torch.Size([1, 236])
returning input_ids
input ids shape:  torch.Size([1, 248])
returning input_ids
input ids shape:  torch.Size([1, 236])
returning input_ids
input ids shape:  torch.Size([1, 326])
returning input_ids
input ids shape:  torch.Size([1, 154])
returning input_ids
input ids shape:  torch.Size([1, 300])
returning input_ids
input ids shape:  torch.Size([1, 376])
"""


input_string4 = """
returning input_ids
input ids shape:  torch.Size([1, 217])
returning input_ids
input ids shape:  torch.Size([1, 141])
returning input_ids
input ids shape:  torch.Size([1, 261])
returning input_ids
input ids shape:  torch.Size([1, 44])
returning input_ids
input ids shape:  torch.Size([1, 363])
returning input_ids
input ids shape:  torch.Size([1, 337])
returning input_ids
input ids shape:  torch.Size([1, 258])
returning input_ids
input ids shape:  torch.Size([1, 225])
returning input_ids
input ids shape:  torch.Size([1, 87])
returning input_ids
input ids shape:  torch.Size([1, 288])
returning input_ids
input ids shape:  torch.Size([1, 369])
returning input_ids
input ids shape:  torch.Size([1, 203])
returning input_ids
input ids shape:  torch.Size([1, 159])
returning input_ids
input ids shape:  torch.Size([1, 361])
returning input_ids
input ids shape:  torch.Size([1, 48])
returning input_ids
input ids shape:  torch.Size([1, 369])
returning input_ids
input ids shape:  torch.Size([1, 133])
returning input_ids
input ids shape:  torch.Size([1, 278])
returning input_ids
input ids shape:  torch.Size([1, 92])
returning input_ids
input ids shape:  torch.Size([1, 299])
returning input_ids
input ids shape:  torch.Size([1, 88])
returning input_ids
input ids shape:  torch.Size([1, 188])
returning input_ids
input ids shape:  torch.Size([1, 130])
returning input_ids
input ids shape:  torch.Size([1, 126])
returning input_ids
input ids shape:  torch.Size([1, 182])
returning input_ids
input ids shape:  torch.Size([1, 143])
returning input_ids
input ids shape:  torch.Size([1, 423])
returning input_ids
input ids shape:  torch.Size([1, 122])
returning input_ids
input ids shape:  torch.Size([1, 91])
returning input_ids
input ids shape:  torch.Size([1, 29])
returning input_ids
input ids shape:  torch.Size([1, 86])
returning input_ids
input ids shape:  torch.Size([1, 2048])
returning input_ids
input ids shape:  torch.Size([1, 306])
returning input_ids
input ids shape:  torch.Size([1, 196])
returning input_ids
input ids shape:  torch.Size([1, 85])
returning input_ids
input ids shape:  torch.Size([1, 192])
returning input_ids
input ids shape:  torch.Size([1, 34])
returning input_ids
input ids shape:  torch.Size([1, 312])
returning input_ids
input ids shape:  torch.Size([1, 165])
returning input_ids
input ids shape:  torch.Size([1, 123])
returning input_ids
input ids shape:  torch.Size([1, 30])
returning input_ids
input ids shape:  torch.Size([1, 436])
returning input_ids
input ids shape:  torch.Size([1, 56])
returning input_ids
input ids shape:  torch.Size([1, 161])
returning input_ids
input ids shape:  torch.Size([1, 174])
returning input_ids
input ids shape:  torch.Size([1, 108])
returning input_ids
input ids shape:  torch.Size([1, 177])
returning input_ids
input ids shape:  torch.Size([1, 50])
returning input_ids
input ids shape:  torch.Size([1, 243])
returning input_ids
input ids shape:  torch.Size([1, 215])
returning input_ids
input ids shape:  torch.Size([1, 205])
returning input_ids
input ids shape:  torch.Size([1, 225])
returning input_ids
input ids shape:  torch.Size([1, 176])
returning input_ids
input ids shape:  torch.Size([1, 36])
returning input_ids
input ids shape:  torch.Size([1, 319])
returning input_ids
input ids shape:  torch.Size([1, 122])
returning input_ids
input ids shape:  torch.Size([1, 112])
returning input_ids
input ids shape:  torch.Size([1, 59])
returning input_ids
input ids shape:  torch.Size([1, 236])
returning input_ids
input ids shape:  torch.Size([1, 412])
returning input_ids
input ids shape:  torch.Size([1, 221])
returning input_ids
input ids shape:  torch.Size([1, 165])
returning input_ids
input ids shape:  torch.Size([1, 246])
returning input_ids
input ids shape:  torch.Size([1, 138])
returning input_ids
input ids shape:  torch.Size([1, 163])
returning input_ids
input ids shape:  torch.Size([1, 102])
returning input_ids
input ids shape:  torch.Size([1, 73])
returning input_ids
input ids shape:  torch.Size([1, 184])
returning input_ids
input ids shape:  torch.Size([1, 179])
returning input_ids
input ids shape:  torch.Size([1, 106])
returning input_ids
input ids shape:  torch.Size([1, 107])
returning input_ids
input ids shape:  torch.Size([1, 301])
returning input_ids
input ids shape:  torch.Size([1, 411])
returning input_ids
input ids shape:  torch.Size([1, 100])
returning input_ids
input ids shape:  torch.Size([1, 11])
returning input_ids
input ids shape:  torch.Size([1, 96])
returning input_ids
input ids shape:  torch.Size([1, 241])
returning input_ids
input ids shape:  torch.Size([1, 649])
returning input_ids
input ids shape:  torch.Size([1, 354])
returning input_ids
input ids shape:  torch.Size([1, 53])
returning input_ids
input ids shape:  torch.Size([1, 167])
returning input_ids
input ids shape:  torch.Size([1, 210])
returning input_ids
input ids shape:  torch.Size([1, 95])
returning input_ids
input ids shape:  torch.Size([1, 281])
returning input_ids
input ids shape:  torch.Size([1, 77])
returning input_ids
input ids shape:  torch.Size([1, 318])
returning input_ids
input ids shape:  torch.Size([1, 155])
returning input_ids
input ids shape:  torch.Size([1, 251])
returning input_ids
input ids shape:  torch.Size([1, 407])
returning input_ids
input ids shape:  torch.Size([1, 146])
returning input_ids
input ids shape:  torch.Size([1, 125])
returning input_ids
input ids shape:  torch.Size([1, 198])
returning input_ids
input ids shape:  torch.Size([1, 201])
returning input_ids
input ids shape:  torch.Size([1, 124])
returning input_ids
input ids shape:  torch.Size([1, 158])
returning input_ids
input ids shape:  torch.Size([1, 198])
returning input_ids
input ids shape:  torch.Size([1, 264])
returning input_ids
input ids shape:  torch.Size([1, 94])
returning input_ids
input ids shape:  torch.Size([1, 148])
returning input_ids
input ids shape:  torch.Size([1, 263])
"""

input_string5 = """
returning input_ids
input ids shape:  torch.Size([1, 217])
returning input_ids
input ids shape:  torch.Size([1, 284])
returning input_ids
input ids shape:  torch.Size([1, 277])
returning input_ids
input ids shape:  torch.Size([1, 212])
returning input_ids
input ids shape:  torch.Size([1, 302])
returning input_ids
input ids shape:  torch.Size([1, 346])
returning input_ids
input ids shape:  torch.Size([1, 276])
returning input_ids
input ids shape:  torch.Size([1, 157])
returning input_ids
input ids shape:  torch.Size([1, 50])
returning input_ids
input ids shape:  torch.Size([1, 454])
returning input_ids
input ids shape:  torch.Size([1, 255])
returning input_ids
input ids shape:  torch.Size([1, 123])
returning input_ids
input ids shape:  torch.Size([1, 166])
returning input_ids
input ids shape:  torch.Size([1, 305])
returning input_ids
input ids shape:  torch.Size([1, 191])
returning input_ids
input ids shape:  torch.Size([1, 308])
returning input_ids
input ids shape:  torch.Size([1, 96])
returning input_ids
input ids shape:  torch.Size([1, 375])
returning input_ids
input ids shape:  torch.Size([1, 43])
returning input_ids
input ids shape:  torch.Size([1, 137])
returning input_ids
input ids shape:  torch.Size([1, 120])
returning input_ids
input ids shape:  torch.Size([1, 131])
returning input_ids
input ids shape:  torch.Size([1, 209])
returning input_ids
input ids shape:  torch.Size([1, 126])
returning input_ids
input ids shape:  torch.Size([1, 121])
returning input_ids
input ids shape:  torch.Size([1, 186])
returning input_ids
input ids shape:  torch.Size([1, 299])
returning input_ids
input ids shape:  torch.Size([1, 137])
returning input_ids
input ids shape:  torch.Size([1, 138])
returning input_ids
input ids shape:  torch.Size([1, 76])
returning input_ids
input ids shape:  torch.Size([1, 67])
returning input_ids
input ids shape:  torch.Size([1, 202])
returning input_ids
input ids shape:  torch.Size([1, 228])
returning input_ids
input ids shape:  torch.Size([1, 249])
returning input_ids
input ids shape:  torch.Size([1, 91])
returning input_ids
input ids shape:  torch.Size([1, 136])
returning input_ids
input ids shape:  torch.Size([1, 56])
returning input_ids
input ids shape:  torch.Size([1, 358])
returning input_ids
input ids shape:  torch.Size([1, 40])
returning input_ids
input ids shape:  torch.Size([1, 46])
returning input_ids
input ids shape:  torch.Size([1, 121])
returning input_ids
input ids shape:  torch.Size([1, 379])
returning input_ids
input ids shape:  torch.Size([1, 75])
returning input_ids
input ids shape:  torch.Size([1, 43])
returning input_ids
input ids shape:  torch.Size([1, 269])
returning input_ids
input ids shape:  torch.Size([1, 176])
returning input_ids
input ids shape:  torch.Size([1, 200])
returning input_ids
input ids shape:  torch.Size([1, 50])
returning input_ids
input ids shape:  torch.Size([1, 272])
returning input_ids
input ids shape:  torch.Size([1, 145])
returning input_ids
input ids shape:  torch.Size([1, 276])
returning input_ids
input ids shape:  torch.Size([1, 319])
returning input_ids
input ids shape:  torch.Size([1, 35])
returning input_ids
input ids shape:  torch.Size([1, 358])
returning input_ids
input ids shape:  torch.Size([1, 190])
returning input_ids
input ids shape:  torch.Size([1, 154])
returning input_ids
input ids shape:  torch.Size([1, 79])
returning input_ids
input ids shape:  torch.Size([1, 130])
returning input_ids
input ids shape:  torch.Size([1, 375])
returning input_ids
input ids shape:  torch.Size([1, 392])
returning input_ids
input ids shape:  torch.Size([1, 192])
returning input_ids
input ids shape:  torch.Size([1, 225])
returning input_ids
input ids shape:  torch.Size([1, 348])
returning input_ids
input ids shape:  torch.Size([1, 345])
returning input_ids
input ids shape:  torch.Size([1, 336])
returning input_ids
input ids shape:  torch.Size([1, 123])
returning input_ids
input ids shape:  torch.Size([1, 146])
returning input_ids
input ids shape:  torch.Size([1, 298])
returning input_ids
input ids shape:  torch.Size([1, 152])
returning input_ids
input ids shape:  torch.Size([1, 115])
returning input_ids
input ids shape:  torch.Size([1, 191])
returning input_ids
input ids shape:  torch.Size([1, 305])
returning input_ids
input ids shape:  torch.Size([1, 318])
returning input_ids
input ids shape:  torch.Size([1, 23])
returning input_ids
input ids shape:  torch.Size([1, 11])
returning input_ids
input ids shape:  torch.Size([1, 57])
returning input_ids
input ids shape:  torch.Size([1, 108])
returning input_ids
input ids shape:  torch.Size([1, 321])
returning input_ids
input ids shape:  torch.Size([1, 302])
returning input_ids
input ids shape:  torch.Size([1, 88])
returning input_ids
input ids shape:  torch.Size([1, 143])
returning input_ids
input ids shape:  torch.Size([1, 241])
returning input_ids
input ids shape:  torch.Size([1, 75])
returning input_ids
input ids shape:  torch.Size([1, 232])
returning input_ids
input ids shape:  torch.Size([1, 55])
returning input_ids
input ids shape:  torch.Size([1, 256])
returning input_ids
input ids shape:  torch.Size([1, 248])
returning input_ids
input ids shape:  torch.Size([1, 237])
returning input_ids
input ids shape:  torch.Size([1, 92])
returning input_ids
input ids shape:  torch.Size([1, 196])
returning input_ids
input ids shape:  torch.Size([1, 179])
returning input_ids
input ids shape:  torch.Size([1, 197])
returning input_ids
input ids shape:  torch.Size([1, 326])
returning input_ids
input ids shape:  torch.Size([1, 247])
returning input_ids
input ids shape:  torch.Size([1, 227])
returning input_ids
input ids shape:  torch.Size([1, 200])
returning input_ids
input ids shape:  torch.Size([1, 335])
returning input_ids
input ids shape:  torch.Size([1, 62])
returning input_ids
input ids shape:  torch.Size([1, 243])
returning input_ids
input ids shape:  torch.Size([1, 271])
"""

input_string6 = """
returning input_ids
input ids shape:  torch.Size([1, 217])
returning input_ids
input ids shape:  torch.Size([1, 284])
returning input_ids
input ids shape:  torch.Size([1, 277])
returning input_ids
input ids shape:  torch.Size([1, 212])
returning input_ids
input ids shape:  torch.Size([1, 302])
returning input_ids
input ids shape:  torch.Size([1, 346])
returning input_ids
input ids shape:  torch.Size([1, 276])
returning input_ids
input ids shape:  torch.Size([1, 157])
returning input_ids
input ids shape:  torch.Size([1, 50])
returning input_ids
input ids shape:  torch.Size([1, 454])
returning input_ids
input ids shape:  torch.Size([1, 255])
returning input_ids
input ids shape:  torch.Size([1, 123])
returning input_ids
input ids shape:  torch.Size([1, 166])
returning input_ids
input ids shape:  torch.Size([1, 305])
returning input_ids
input ids shape:  torch.Size([1, 191])
returning input_ids
input ids shape:  torch.Size([1, 308])
returning input_ids
input ids shape:  torch.Size([1, 96])
returning input_ids
input ids shape:  torch.Size([1, 375])
returning input_ids
input ids shape:  torch.Size([1, 43])
returning input_ids
input ids shape:  torch.Size([1, 137])
returning input_ids
input ids shape:  torch.Size([1, 120])
returning input_ids
input ids shape:  torch.Size([1, 131])
returning input_ids
input ids shape:  torch.Size([1, 209])
returning input_ids
input ids shape:  torch.Size([1, 126])
returning input_ids
input ids shape:  torch.Size([1, 121])
returning input_ids
input ids shape:  torch.Size([1, 186])
returning input_ids
input ids shape:  torch.Size([1, 299])
returning input_ids
input ids shape:  torch.Size([1, 137])
returning input_ids
input ids shape:  torch.Size([1, 138])
returning input_ids
input ids shape:  torch.Size([1, 76])
returning input_ids
input ids shape:  torch.Size([1, 67])
returning input_ids
input ids shape:  torch.Size([1, 202])
returning input_ids
input ids shape:  torch.Size([1, 228])
returning input_ids
input ids shape:  torch.Size([1, 249])
returning input_ids
input ids shape:  torch.Size([1, 91])
returning input_ids
input ids shape:  torch.Size([1, 136])
returning input_ids
input ids shape:  torch.Size([1, 56])
returning input_ids
input ids shape:  torch.Size([1, 358])
returning input_ids
input ids shape:  torch.Size([1, 40])
returning input_ids
input ids shape:  torch.Size([1, 46])
returning input_ids
input ids shape:  torch.Size([1, 121])
returning input_ids
input ids shape:  torch.Size([1, 379])
returning input_ids
input ids shape:  torch.Size([1, 75])
returning input_ids
input ids shape:  torch.Size([1, 43])
returning input_ids
input ids shape:  torch.Size([1, 269])
returning input_ids
input ids shape:  torch.Size([1, 176])
returning input_ids
input ids shape:  torch.Size([1, 200])
returning input_ids
input ids shape:  torch.Size([1, 50])
returning input_ids
input ids shape:  torch.Size([1, 272])
returning input_ids
input ids shape:  torch.Size([1, 145])
returning input_ids
input ids shape:  torch.Size([1, 276])
returning input_ids
input ids shape:  torch.Size([1, 319])
returning input_ids
input ids shape:  torch.Size([1, 35])
returning input_ids
input ids shape:  torch.Size([1, 358])
returning input_ids
input ids shape:  torch.Size([1, 190])
returning input_ids
input ids shape:  torch.Size([1, 154])
returning input_ids
input ids shape:  torch.Size([1, 79])
returning input_ids
input ids shape:  torch.Size([1, 130])
returning input_ids
input ids shape:  torch.Size([1, 375])
returning input_ids
input ids shape:  torch.Size([1, 392])
returning input_ids
input ids shape:  torch.Size([1, 192])
returning input_ids
input ids shape:  torch.Size([1, 225])
returning input_ids
input ids shape:  torch.Size([1, 348])
returning input_ids
input ids shape:  torch.Size([1, 345])
returning input_ids
input ids shape:  torch.Size([1, 336])
returning input_ids
input ids shape:  torch.Size([1, 123])
returning input_ids
input ids shape:  torch.Size([1, 146])
returning input_ids
input ids shape:  torch.Size([1, 298])
returning input_ids
input ids shape:  torch.Size([1, 152])
returning input_ids
input ids shape:  torch.Size([1, 115])
returning input_ids
input ids shape:  torch.Size([1, 191])
returning input_ids
input ids shape:  torch.Size([1, 305])
returning input_ids
input ids shape:  torch.Size([1, 318])
returning input_ids
input ids shape:  torch.Size([1, 23])
returning input_ids
input ids shape:  torch.Size([1, 11])
returning input_ids
input ids shape:  torch.Size([1, 57])
returning input_ids
input ids shape:  torch.Size([1, 108])
returning input_ids
input ids shape:  torch.Size([1, 321])
returning input_ids
input ids shape:  torch.Size([1, 302])
returning input_ids
input ids shape:  torch.Size([1, 88])
returning input_ids
input ids shape:  torch.Size([1, 143])
returning input_ids
input ids shape:  torch.Size([1, 241])
returning input_ids
input ids shape:  torch.Size([1, 75])
returning input_ids
input ids shape:  torch.Size([1, 232])
returning input_ids
input ids shape:  torch.Size([1, 55])
returning input_ids
input ids shape:  torch.Size([1, 256])
returning input_ids
input ids shape:  torch.Size([1, 248])
returning input_ids
input ids shape:  torch.Size([1, 237])
returning input_ids
input ids shape:  torch.Size([1, 92])
returning input_ids
input ids shape:  torch.Size([1, 196])
returning input_ids
input ids shape:  torch.Size([1, 179])
returning input_ids
input ids shape:  torch.Size([1, 197])
returning input_ids
input ids shape:  torch.Size([1, 326])
returning input_ids
input ids shape:  torch.Size([1, 247])
returning input_ids
input ids shape:  torch.Size([1, 227])
returning input_ids
input ids shape:  torch.Size([1, 200])
returning input_ids
input ids shape:  torch.Size([1, 335])
returning input_ids
input ids shape:  torch.Size([1, 62])
returning input_ids
input ids shape:  torch.Size([1, 243])
returning input_ids
input ids shape:  torch.Size([1, 271])
baseline time: 699.8809492588043
==========================================================
returning input_ids
input ids shape:  torch.Size([1, 252])
returning input_ids
input ids shape:  torch.Size([1, 252])
returning input_ids
input ids shape:  torch.Size([1, 78])
returning input_ids
input ids shape:  torch.Size([1, 212])
returning input_ids
input ids shape:  torch.Size([1, 209])
returning input_ids
input ids shape:  torch.Size([1, 483])
returning input_ids
input ids shape:  torch.Size([1, 274])
returning input_ids
input ids shape:  torch.Size([1, 217])
returning input_ids
input ids shape:  torch.Size([1, 100])
returning input_ids
input ids shape:  torch.Size([1, 439])
returning input_ids
input ids shape:  torch.Size([1, 251])
returning input_ids
input ids shape:  torch.Size([1, 155])
returning input_ids
input ids shape:  torch.Size([1, 259])
returning input_ids
input ids shape:  torch.Size([1, 238])
returning input_ids
input ids shape:  torch.Size([1, 78])
returning input_ids
input ids shape:  torch.Size([1, 335])
returning input_ids
input ids shape:  torch.Size([1, 136])
returning input_ids
input ids shape:  torch.Size([1, 283])
returning input_ids
input ids shape:  torch.Size([1, 147])
returning input_ids
input ids shape:  torch.Size([1, 590])
returning input_ids
input ids shape:  torch.Size([1, 122])
returning input_ids
input ids shape:  torch.Size([1, 92])
returning input_ids
input ids shape:  torch.Size([1, 157])
returning input_ids
input ids shape:  torch.Size([1, 80])
returning input_ids
input ids shape:  torch.Size([1, 104])
returning input_ids
input ids shape:  torch.Size([1, 122])
returning input_ids
input ids shape:  torch.Size([1, 2048])
returning input_ids
input ids shape:  torch.Size([1, 86])
returning input_ids
input ids shape:  torch.Size([1, 75])
returning input_ids
input ids shape:  torch.Size([1, 31])
returning input_ids
input ids shape:  torch.Size([1, 74])
returning input_ids
input ids shape:  torch.Size([1, 28])
returning input_ids
input ids shape:  torch.Size([1, 408])
returning input_ids
input ids shape:  torch.Size([1, 232])
returning input_ids
input ids shape:  torch.Size([1, 105])
returning input_ids
input ids shape:  torch.Size([1, 230])
returning input_ids
input ids shape:  torch.Size([1, 18])
returning input_ids
input ids shape:  torch.Size([1, 151])
returning input_ids
input ids shape:  torch.Size([1, 288])
returning input_ids
input ids shape:  torch.Size([1, 102])
returning input_ids
input ids shape:  torch.Size([1, 30])
returning input_ids
input ids shape:  torch.Size([1, 421])
returning input_ids
input ids shape:  torch.Size([1, 77])
returning input_ids
input ids shape:  torch.Size([1, 25])
returning input_ids
input ids shape:  torch.Size([1, 160])
returning input_ids
input ids shape:  torch.Size([1, 132])
returning input_ids
input ids shape:  torch.Size([1, 278])
returning input_ids
input ids shape:  torch.Size([1, 50])
returning input_ids
input ids shape:  torch.Size([1, 242])
returning input_ids
input ids shape:  torch.Size([1, 82])
returning input_ids
input ids shape:  torch.Size([1, 293])
returning input_ids
input ids shape:  torch.Size([1, 275])
returning input_ids
input ids shape:  torch.Size([1, 99])
returning input_ids
input ids shape:  torch.Size([1, 311])
returning input_ids
input ids shape:  torch.Size([1, 204])
returning input_ids
input ids shape:  torch.Size([1, 109])
returning input_ids
input ids shape:  torch.Size([1, 96])
returning input_ids
input ids shape:  torch.Size([1, 69])
returning input_ids
input ids shape:  torch.Size([1, 232])
returning input_ids
input ids shape:  torch.Size([1, 389])
returning input_ids
input ids shape:  torch.Size([1, 259])
returning input_ids
input ids shape:  torch.Size([1, 255])
returning input_ids
input ids shape:  torch.Size([1, 188])
returning input_ids
input ids shape:  torch.Size([1, 239])
returning input_ids
input ids shape:  torch.Size([1, 288])
returning input_ids
input ids shape:  torch.Size([1, 279])
returning input_ids
input ids shape:  torch.Size([1, 72])
returning input_ids
input ids shape:  torch.Size([1, 309])
returning input_ids
input ids shape:  torch.Size([1, 68])
returning input_ids
input ids shape:  torch.Size([1, 114])
returning input_ids
input ids shape:  torch.Size([1, 88])
returning input_ids
input ids shape:  torch.Size([1, 335])
returning input_ids
input ids shape:  torch.Size([1, 324])
returning input_ids
input ids shape:  torch.Size([1, 96])
returning input_ids
input ids shape:  torch.Size([1, 11])
returning input_ids
input ids shape:  torch.Size([1, 100])
returning input_ids
input ids shape:  torch.Size([1, 404])
returning input_ids
input ids shape:  torch.Size([1, 446])
returning input_ids
input ids shape:  torch.Size([1, 249])
returning input_ids
input ids shape:  torch.Size([1, 88])
returning input_ids
input ids shape:  torch.Size([1, 154])
returning input_ids
input ids shape:  torch.Size([1, 301])
returning input_ids
input ids shape:  torch.Size([1, 93])
returning input_ids
input ids shape:  torch.Size([1, 371])
returning input_ids
input ids shape:  torch.Size([1, 63])
returning input_ids
input ids shape:  torch.Size([1, 187])
returning input_ids
input ids shape:  torch.Size([1, 248])
returning input_ids
input ids shape:  torch.Size([1, 331])
returning input_ids
input ids shape:  torch.Size([1, 365])
returning input_ids
input ids shape:  torch.Size([1, 53])
returning input_ids
input ids shape:  torch.Size([1, 212])
returning input_ids
input ids shape:  torch.Size([1, 192])
returning input_ids
input ids shape:  torch.Size([1, 316])
returning input_ids
input ids shape:  torch.Size([1, 281])
returning input_ids
input ids shape:  torch.Size([1, 229])
returning input_ids
input ids shape:  torch.Size([1, 276])
returning input_ids
input ids shape:  torch.Size([1, 267])
returning input_ids
input ids shape:  torch.Size([1, 109])
returning input_ids
input ids shape:  torch.Size([1, 134])
returning input_ids
input ids shape:  torch.Size([1, 297])
"""


input_string7 = """
returning input_ids
input ids shape:  torch.Size([1, 197])
returning input_ids
input ids shape:  torch.Size([1, 288])
returning input_ids
input ids shape:  torch.Size([1, 171])
returning input_ids
input ids shape:  torch.Size([1, 424])
returning input_ids
input ids shape:  torch.Size([1, 370])
returning input_ids
input ids shape:  torch.Size([1, 407])
returning input_ids
input ids shape:  torch.Size([1, 156])
returning input_ids
input ids shape:  torch.Size([1, 153])
returning input_ids
input ids shape:  torch.Size([1, 104])
returning input_ids
input ids shape:  torch.Size([1, 213])
returning input_ids
input ids shape:  torch.Size([1, 283])
returning input_ids
input ids shape:  torch.Size([1, 502])
returning input_ids
input ids shape:  torch.Size([1, 127])
returning input_ids
input ids shape:  torch.Size([1, 296])
returning input_ids
input ids shape:  torch.Size([1, 430])
returning input_ids
input ids shape:  torch.Size([1, 365])
returning input_ids
input ids shape:  torch.Size([1, 65])
returning input_ids
input ids shape:  torch.Size([1, 295])
returning input_ids
input ids shape:  torch.Size([1, 223])
returning input_ids
input ids shape:  torch.Size([1, 197])
returning input_ids
input ids shape:  torch.Size([1, 152])
returning input_ids
input ids shape:  torch.Size([1, 92])
returning input_ids
input ids shape:  torch.Size([1, 229])
returning input_ids
input ids shape:  torch.Size([1, 113])
returning input_ids
input ids shape:  torch.Size([1, 150])
returning input_ids
input ids shape:  torch.Size([1, 216])
returning input_ids
input ids shape:  torch.Size([1, 322])
returning input_ids
input ids shape:  torch.Size([1, 86])
returning input_ids
input ids shape:  torch.Size([1, 140])
returning input_ids
input ids shape:  torch.Size([1, 79])
returning input_ids
input ids shape:  torch.Size([1, 59])
returning input_ids
input ids shape:  torch.Size([1, 52])
returning input_ids
input ids shape:  torch.Size([1, 350])
returning input_ids
input ids shape:  torch.Size([1, 322])
returning input_ids
input ids shape:  torch.Size([1, 139])
returning input_ids
input ids shape:  torch.Size([1, 224])
returning input_ids
input ids shape:  torch.Size([1, 353])
returning input_ids
input ids shape:  torch.Size([1, 183])
returning input_ids
input ids shape:  torch.Size([1, 350])
returning input_ids
input ids shape:  torch.Size([1, 41])
returning input_ids
input ids shape:  torch.Size([1, 29])
returning input_ids
input ids shape:  torch.Size([1, 352])
returning input_ids
input ids shape:  torch.Size([1, 156])
returning input_ids
input ids shape:  torch.Size([1, 43])
returning input_ids
input ids shape:  torch.Size([1, 469])
returning input_ids
input ids shape:  torch.Size([1, 109])
returning input_ids
input ids shape:  torch.Size([1, 365])
returning input_ids
input ids shape:  torch.Size([1, 185])
returning input_ids
input ids shape:  torch.Size([1, 318])
returning input_ids
input ids shape:  torch.Size([1, 148])
returning input_ids
input ids shape:  torch.Size([1, 351])
returning input_ids
input ids shape:  torch.Size([1, 195])
returning input_ids
input ids shape:  torch.Size([1, 42])
returning input_ids
input ids shape:  torch.Size([1, 162])
returning input_ids
input ids shape:  torch.Size([1, 215])
returning input_ids
input ids shape:  torch.Size([1, 234])
returning input_ids
input ids shape:  torch.Size([1, 81])
returning input_ids
input ids shape:  torch.Size([1, 89])
returning input_ids
input ids shape:  torch.Size([1, 2048])
returning input_ids
input ids shape:  torch.Size([1, 391])
returning input_ids
input ids shape:  torch.Size([1, 199])
returning input_ids
input ids shape:  torch.Size([1, 180])
returning input_ids
input ids shape:  torch.Size([1, 216])
returning input_ids
input ids shape:  torch.Size([1, 253])
returning input_ids
input ids shape:  torch.Size([1, 292])
returning input_ids
input ids shape:  torch.Size([1, 110])
returning input_ids
input ids shape:  torch.Size([1, 60])
returning input_ids
input ids shape:  torch.Size([1, 241])
returning input_ids
input ids shape:  torch.Size([1, 239])
returning input_ids
input ids shape:  torch.Size([1, 145])
returning input_ids
input ids shape:  torch.Size([1, 104])
returning input_ids
input ids shape:  torch.Size([1, 315])
returning input_ids
input ids shape:  torch.Size([1, 460])
returning input_ids
input ids shape:  torch.Size([1, 86])
returning input_ids
input ids shape:  torch.Size([1, 11])
returning input_ids
input ids shape:  torch.Size([1, 30])
returning input_ids
input ids shape:  torch.Size([1, 74])
returning input_ids
input ids shape:  torch.Size([1, 273])
returning input_ids
input ids shape:  torch.Size([1, 263])
returning input_ids
input ids shape:  torch.Size([1, 40])
returning input_ids
input ids shape:  torch.Size([1, 143])
returning input_ids
input ids shape:  torch.Size([1, 269])
returning input_ids
input ids shape:  torch.Size([1, 81])
returning input_ids
input ids shape:  torch.Size([1, 181])
returning input_ids
input ids shape:  torch.Size([1, 73])
returning input_ids
input ids shape:  torch.Size([1, 261])
returning input_ids
input ids shape:  torch.Size([1, 176])
returning input_ids
input ids shape:  torch.Size([1, 213])
returning input_ids
input ids shape:  torch.Size([1, 146])
returning input_ids
input ids shape:  torch.Size([1, 44])
returning input_ids
input ids shape:  torch.Size([1, 253])
returning input_ids
input ids shape:  torch.Size([1, 274])
returning input_ids
input ids shape:  torch.Size([1, 240])
returning input_ids
input ids shape:  torch.Size([1, 252])
returning input_ids
input ids shape:  torch.Size([1, 168])
returning input_ids
input ids shape:  torch.Size([1, 269])
returning input_ids
input ids shape:  torch.Size([1, 269])
returning input_ids
input ids shape:  torch.Size([1, 114])
returning input_ids
input ids shape:  torch.Size([1, 142])
returning input_ids
input ids shape:  torch.Size([1, 279])
"""


input_string8 = """
returning input_ids
input ids shape:  torch.Size([1, 249])
returning input_ids
input ids shape:  torch.Size([1, 173])
returning input_ids
input ids shape:  torch.Size([1, 226])
returning input_ids
input ids shape:  torch.Size([1, 328])
returning input_ids
input ids shape:  torch.Size([1, 292])
returning input_ids
input ids shape:  torch.Size([1, 210])
returning input_ids
input ids shape:  torch.Size([1, 79])
returning input_ids
input ids shape:  torch.Size([1, 194])
returning input_ids
input ids shape:  torch.Size([1, 77])
returning input_ids
input ids shape:  torch.Size([1, 500])
returning input_ids
input ids shape:  torch.Size([1, 221])
returning input_ids
input ids shape:  torch.Size([1, 99])
returning input_ids
input ids shape:  torch.Size([1, 288])
returning input_ids
input ids shape:  torch.Size([1, 355])
returning input_ids
input ids shape:  torch.Size([1, 243])
returning input_ids
input ids shape:  torch.Size([1, 514])
returning input_ids
input ids shape:  torch.Size([1, 423])
returning input_ids
input ids shape:  torch.Size([1, 217])
returning input_ids
input ids shape:  torch.Size([1, 90])
returning input_ids
input ids shape:  torch.Size([1, 967])
returning input_ids
input ids shape:  torch.Size([1, 57])
returning input_ids
input ids shape:  torch.Size([1, 117])
returning input_ids
input ids shape:  torch.Size([1, 269])
returning input_ids
input ids shape:  torch.Size([1, 118])
returning input_ids
input ids shape:  torch.Size([1, 130])
returning input_ids
input ids shape:  torch.Size([1, 93])
returning input_ids
input ids shape:  torch.Size([1, 2048])
returning input_ids
input ids shape:  torch.Size([1, 118])
returning input_ids
input ids shape:  torch.Size([1, 99])
returning input_ids
input ids shape:  torch.Size([1, 31])
returning input_ids
input ids shape:  torch.Size([1, 41])
returning input_ids
input ids shape:  torch.Size([1, 34])
returning input_ids
input ids shape:  torch.Size([1, 398])
returning input_ids
input ids shape:  torch.Size([1, 190])
returning input_ids
input ids shape:  torch.Size([1, 137])
returning input_ids
input ids shape:  torch.Size([1, 135])
returning input_ids
input ids shape:  torch.Size([1, 85])
returning input_ids
input ids shape:  torch.Size([1, 90])
returning input_ids
input ids shape:  torch.Size([1, 2048])
returning input_ids
input ids shape:  torch.Size([1, 95])
returning input_ids
input ids shape:  torch.Size([1, 36])
returning input_ids
input ids shape:  torch.Size([1, 570])
returning input_ids
input ids shape:  torch.Size([1, 24])
returning input_ids
input ids shape:  torch.Size([1, 81])
returning input_ids
input ids shape:  torch.Size([1, 487])
returning input_ids
input ids shape:  torch.Size([1, 136])
returning input_ids
input ids shape:  torch.Size([1, 1263])
returning input_ids
input ids shape:  torch.Size([1, 180])
returning input_ids
input ids shape:  torch.Size([1, 409])
returning input_ids
input ids shape:  torch.Size([1, 220])
returning input_ids
input ids shape:  torch.Size([1, 399])
returning input_ids
input ids shape:  torch.Size([1, 441])
returning input_ids
input ids shape:  torch.Size([1, 144])
returning input_ids
input ids shape:  torch.Size([1, 264])
returning input_ids
input ids shape:  torch.Size([1, 264])
returning input_ids
input ids shape:  torch.Size([1, 239])
returning input_ids
input ids shape:  torch.Size([1, 88])
returning input_ids
input ids shape:  torch.Size([1, 59])
returning input_ids
input ids shape:  torch.Size([1, 179])
returning input_ids
input ids shape:  torch.Size([1, 463])
returning input_ids
input ids shape:  torch.Size([1, 128])
returning input_ids
input ids shape:  torch.Size([1, 169])
returning input_ids
input ids shape:  torch.Size([1, 329])
returning input_ids
input ids shape:  torch.Size([1, 245])
returning input_ids
input ids shape:  torch.Size([1, 233])
returning input_ids
input ids shape:  torch.Size([1, 135])
returning input_ids
input ids shape:  torch.Size([1, 51])
returning input_ids
input ids shape:  torch.Size([1, 190])
returning input_ids
input ids shape:  torch.Size([1, 82])
returning input_ids
input ids shape:  torch.Size([1, 110])
returning input_ids
input ids shape:  torch.Size([1, 243])
returning input_ids
input ids shape:  torch.Size([1, 282])
returning input_ids
input ids shape:  torch.Size([1, 285])
returning input_ids
input ids shape:  torch.Size([1, 53])
returning input_ids
input ids shape:  torch.Size([1, 11])
returning input_ids
input ids shape:  torch.Size([1, 98])
returning input_ids
input ids shape:  torch.Size([1, 153])
returning input_ids
input ids shape:  torch.Size([1, 566])
returning input_ids
input ids shape:  torch.Size([1, 278])
returning input_ids
input ids shape:  torch.Size([1, 57])
returning input_ids
input ids shape:  torch.Size([1, 162])
returning input_ids
input ids shape:  torch.Size([1, 228])
returning input_ids
input ids shape:  torch.Size([1, 71])
returning input_ids
input ids shape:  torch.Size([1, 336])
returning input_ids
input ids shape:  torch.Size([1, 32])
returning input_ids
input ids shape:  torch.Size([1, 166])
returning input_ids
input ids shape:  torch.Size([1, 225])
returning input_ids
input ids shape:  torch.Size([1, 242])
returning input_ids
input ids shape:  torch.Size([1, 233])
returning input_ids
input ids shape:  torch.Size([1, 38])
returning input_ids
input ids shape:  torch.Size([1, 235])
returning input_ids
input ids shape:  torch.Size([1, 206])
returning input_ids
input ids shape:  torch.Size([1, 490])
returning input_ids
input ids shape:  torch.Size([1, 213])
returning input_ids
input ids shape:  torch.Size([1, 175])
returning input_ids
input ids shape:  torch.Size([1, 126])
returning input_ids
input ids shape:  torch.Size([1, 250])
returning input_ids
input ids shape:  torch.Size([1, 2048])
returning input_ids
input ids shape:  torch.Size([1, 161])
returning input_ids
input ids shape:  torch.Size([1, 281])
"""
input_string9 = """
returning input_ids
input ids shape:  torch.Size([1, 248])
returning input_ids
input ids shape:  torch.Size([1, 237])
returning input_ids
input ids shape:  torch.Size([1, 223])
returning input_ids
input ids shape:  torch.Size([1, 243])
returning input_ids
input ids shape:  torch.Size([1, 254])
returning input_ids
input ids shape:  torch.Size([1, 105])
returning input_ids
input ids shape:  torch.Size([1, 116])
returning input_ids
input ids shape:  torch.Size([1, 130])
returning input_ids
input ids shape:  torch.Size([1, 98])
returning input_ids
input ids shape:  torch.Size([1, 58])
returning input_ids
input ids shape:  torch.Size([1, 350])
returning input_ids
input ids shape:  torch.Size([1, 171])
returning input_ids
input ids shape:  torch.Size([1, 222])
returning input_ids
input ids shape:  torch.Size([1, 301])
returning input_ids
input ids shape:  torch.Size([1, 50])
returning input_ids
input ids shape:  torch.Size([1, 247])
returning input_ids
input ids shape:  torch.Size([1, 101])
returning input_ids
input ids shape:  torch.Size([1, 319])
returning input_ids
input ids shape:  torch.Size([1, 193])
returning input_ids
input ids shape:  torch.Size([1, 389])
returning input_ids
input ids shape:  torch.Size([1, 147])
returning input_ids
input ids shape:  torch.Size([1, 168])
returning input_ids
input ids shape:  torch.Size([1, 134])
returning input_ids
input ids shape:  torch.Size([1, 79])
returning input_ids
input ids shape:  torch.Size([1, 191])
returning input_ids
input ids shape:  torch.Size([1, 167])
returning input_ids
input ids shape:  torch.Size([1, 217])
returning input_ids
input ids shape:  torch.Size([1, 160])
returning input_ids
input ids shape:  torch.Size([1, 121])
returning input_ids
input ids shape:  torch.Size([1, 34])
returning input_ids
input ids shape:  torch.Size([1, 118])
returning input_ids
input ids shape:  torch.Size([1, 154])
returning input_ids
input ids shape:  torch.Size([1, 324])
returning input_ids
input ids shape:  torch.Size([1, 218])
returning input_ids
input ids shape:  torch.Size([1, 103])
returning input_ids
input ids shape:  torch.Size([1, 159])
returning input_ids
input ids shape:  torch.Size([1, 50])
returning input_ids
input ids shape:  torch.Size([1, 159])
returning input_ids
input ids shape:  torch.Size([1, 251])
returning input_ids
input ids shape:  torch.Size([1, 95])
returning input_ids
input ids shape:  torch.Size([1, 163])
returning input_ids
input ids shape:  torch.Size([1, 527])
returning input_ids
input ids shape:  torch.Size([1, 77])
returning input_ids
input ids shape:  torch.Size([1, 30])
returning input_ids
input ids shape:  torch.Size([1, 133])
returning input_ids
input ids shape:  torch.Size([1, 186])
returning input_ids
input ids shape:  torch.Size([1, 455])
returning input_ids
input ids shape:  torch.Size([1, 50])
returning input_ids
input ids shape:  torch.Size([1, 213])
returning input_ids
input ids shape:  torch.Size([1, 233])
returning input_ids
input ids shape:  torch.Size([1, 275])
returning input_ids
input ids shape:  torch.Size([1, 78])
returning input_ids
input ids shape:  torch.Size([1, 95])
returning input_ids
input ids shape:  torch.Size([1, 341])
returning input_ids
input ids shape:  torch.Size([1, 266])
returning input_ids
input ids shape:  torch.Size([1, 225])
returning input_ids
input ids shape:  torch.Size([1, 92])
returning input_ids
input ids shape:  torch.Size([1, 93])
returning input_ids
input ids shape:  torch.Size([1, 422])
returning input_ids
input ids shape:  torch.Size([1, 407])
returning input_ids
input ids shape:  torch.Size([1, 655])
returning input_ids
input ids shape:  torch.Size([1, 226])
returning input_ids
input ids shape:  torch.Size([1, 134])
returning input_ids
input ids shape:  torch.Size([1, 173])
returning input_ids
input ids shape:  torch.Size([1, 335])
returning input_ids
input ids shape:  torch.Size([1, 106])
returning input_ids
input ids shape:  torch.Size([1, 132])
returning input_ids
input ids shape:  torch.Size([1, 340])
returning input_ids
input ids shape:  torch.Size([1, 212])
returning input_ids
input ids shape:  torch.Size([1, 135])
returning input_ids
input ids shape:  torch.Size([1, 140])
returning input_ids
input ids shape:  torch.Size([1, 274])
returning input_ids
input ids shape:  torch.Size([1, 444])
returning input_ids
input ids shape:  torch.Size([1, 82])
returning input_ids
input ids shape:  torch.Size([1, 30])
returning input_ids
input ids shape:  torch.Size([1, 48])
returning input_ids
input ids shape:  torch.Size([1, 74])
returning input_ids
input ids shape:  torch.Size([1, 583])
returning input_ids
input ids shape:  torch.Size([1, 197])
returning input_ids
input ids shape:  torch.Size([1, 89])
returning input_ids
input ids shape:  torch.Size([1, 130])
returning input_ids
input ids shape:  torch.Size([1, 228])
returning input_ids
input ids shape:  torch.Size([1, 104])
returning input_ids
input ids shape:  torch.Size([1, 324])
returning input_ids
input ids shape:  torch.Size([1, 67])
returning input_ids
input ids shape:  torch.Size([1, 312])
returning input_ids
input ids shape:  torch.Size([1, 201])
returning input_ids
input ids shape:  torch.Size([1, 268])
returning input_ids
input ids shape:  torch.Size([1, 124])
returning input_ids
input ids shape:  torch.Size([1, 57])
returning input_ids
input ids shape:  torch.Size([1, 264])
returning input_ids
input ids shape:  torch.Size([1, 268])
returning input_ids
input ids shape:  torch.Size([1, 309])
returning input_ids
input ids shape:  torch.Size([1, 175])
returning input_ids
input ids shape:  torch.Size([1, 167])
returning input_ids
input ids shape:  torch.Size([1, 128])
returning input_ids
input ids shape:  torch.Size([1, 261])
returning input_ids
input ids shape:  torch.Size([1, 63])
returning input_ids
input ids shape:  torch.Size([1, 186])
returning input_ids
input ids shape:  torch.Size([1, 323])
"""

A1 = deal(input_string1)
A2 = deal(input_string2)  
A3 = deal(input_string3)
A4 = deal(input_string4)
A5 = deal(input_string5)
A6 = deal(input_string6)
A7 = deal(input_string7)
A8 = deal(input_string8)
A9 = deal(input_string9)



max_values = [max(a1, a2, a3, a4, a5, a6,a7,a8,a9) for a1, a2 ,a3 ,a4, a5,a6,a7,a8,a9 in zip(A1, A2, A3, A4, A5, A6 ,A7,A8,A9)]

import math
avg_values = [math.ceil((a1+a2+a3+a4+a5+a6+a7+a8+a9)/9) for a1, a2, a3, a4, a5, a6 ,a7,a8,a9 in zip(A1, A2, A3, A4, A5, A6,A7,A8,A9) ]


 
values = [math.ceil(math.ceil((a1+a2+a3+a4+a5+a6+a7+a8+a9)/9)/2 + max(a1, a2, a3, a4, a5, a6 ,a7,a8,a9)/2) for a1, a2, a3, a4, a5, a6 ,a7,a8,a9 in zip(A1, A2, A3, A4, A5, A6,A7,A8,A9) ]

#for a1, a2, a3, a4, a5 in zip(A1, A2, A3, A4, A5):
#    print(a1, a2, a3, a4, a5,"Maximum：",max(a1, a2, a3, a4, a5),"Average Value：",math.ceil((a1+a2+a3+a4+a5)/5),"value: ",math.ceil((a1+a2+a3+a4+a5)/5)/2 + max(a1, a2, a3, a4, a5)/2)
#    print("================================================================")
    
#print("===================")
#print(max_values)

tojson(values)