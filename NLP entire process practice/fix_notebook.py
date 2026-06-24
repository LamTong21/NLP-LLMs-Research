import json

# Replace with your actual notebook filename
filename = '/Users/sonlamtong/Desktop/code doc/NLP & LLMs/NLP entire process practice/Text encoding_ Vectorization .ipynb' 

# Load the notebook
with open(filename, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Check for and delete the widgets metadata
if 'metadata' in nb and 'widgets' in nb['metadata']:
    del nb['metadata']['widgets']
    print("Widgets metadata removed!")
else:
    print("No widgets metadata found.")

# Save the fixed notebook
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)