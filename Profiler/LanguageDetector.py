import sys
from langdetect import detect

# Get the arguments passed to the Python script (i.e. the prompt string)
prompt = sys.argv[1]

# Detect language
detected_language = detect(prompt)

# Output test results
print(detected_language)

