import json 
with open('chapter.json', 'r') as file:
    data = json.load(file)
    print(len(data["chapters"]))