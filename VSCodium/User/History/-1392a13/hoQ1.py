def load_json(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data

points_file = 'points.json'
user_chapter = str(760426163369017375)
user_data = pointdata.get(user_chapter, {"chapter": 0})
pointdata = load_json(points_file)

print(user_data)