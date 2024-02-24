import json 
with open('chapter.json', 'r') as file:
    data = json.load(file)
    print(data["facetoface"])