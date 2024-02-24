import json
def load_json(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data

missions_file = 'chapter.json'
points_file = 'points.json'

chapterdata = load_json(missions_file)
pointdata = load_json(points_file)
user_chapter = str(760426163369017375)
user_data = pointdata.get(user_chapter, {"chapter": 0})

print(user_data)
#print(chapterdata)