from langchain.splitter import JSONSplitter

# Example JSON file
input_json = [
    {"name": "Item1", "content": "Some content", "image": "path/to/image1.jpg"},
    {"name": "Item2", "content": "Other content", "image": "path/to/image2.jpg"},
    {"name": "Item3", "content": "More content", "image": "path/to/image3.jpg"},
]

# Initialize the JSONSplitter
splitter = JSONSplitter(item_key=None)  # 'item_key' should be None to split by each item

# Split the JSON file
split_json = splitter.split(input_json)

# Output the split result
for item in split_json:
    print(item)
