import json
with open("input.json") as f:
    data = json.load(f)

print(data['/project/']["post"]["name"])