import json

boxes = [
    {"name": "Arya Stark", "weight": 12, "width": 4, "length": 3, "height": 2},
    {"name": "Jon Snow", "weight": 14, "width": 5, "length": 4, "height": 2},
    {"name": "Daenerys Targaryen", "weight": 10, "width": 3, "length": 2, "height": 1},
    {"name": "Tyrion Lannister", "weight": 8, "width": 2, "length": 2, "height": 2},
    {"name": "Cersei Lannister", "weight": 11, "width": 3, "length": 2, "height": 2},
    {"name": "Sansa Stark", "weight": 13, "width": 4, "length": 3, "height": 2},
    {"name": "Bran Stark", "weight": 9, "width": 3, "length": 2, "height": 1},
    {"name": "Jaime Lannister", "weight": 15, "width": 5, "length": 3, "height": 3},
    {"name": "Samwell Tarly", "weight": 18, "width": 2, "length": 4, "height": 3},
    {"name": "Jorah Mormont", "weight": 12, "width": 4, "length": 3, "height": 2},
    {"name": "Theon Greyjoy", "weight": 11, "width": 4, "length": 3, "height": 2},
    {"name": "Brienne of Tarth", "weight": 16, "width": 3, "length": 3, "height": 3},
    {"name": "Sandor Clegane", "weight": 17, "width": 4, "length": 4, "height": 3},
    {"name": "Petyr Baelish", "weight": 10, "width": 3, "length": 2, "height": 2},
    {"name": "Varys", "weight": 12, "width": 4, "length": 3, "height": 2},
    {"name": "Melisandre", "weight": 9, "width": 3, "length": 2, "height": 1},
    {"name": "Bronn", "weight": 13, "width": 4, "length": 3, "height": 2},
    {"name": "Gendry", "weight": 14, "width": 4, "length": 3, "height": 2},
    {"name": "Davos Seaworth", "weight": 12, "width": 4, "length": 3, "height": 2},
    {"name": "Tormund Giantsbane", "weight": 18, "width": 3, "length": 5, "height": 3},
    {"name": "Ygritte", "weight": 10, "width": 3, "length": 2, "height": 2},
    {"name": "Missandei", "weight": 8, "width": 3, "length": 2, "height": 2},
    {"name": "Grey Worm", "weight": 13, "width": 4, "length": 3, "height": 2},
    {"name": "Margaery Tyrell", "weight": 9, "width": 3, "length": 2, "height": 2},
    {"name": "Olenna Tyrell", "weight": 11, "width": 3, "length": 2, "height": 2},
]
with open("./boxes.json", "w+") as file:
    file.write(json.dumps(boxes))

freights = [
    {"id": 1, "container_id": 10, "box_id": 1},
    {"id": 2, "container_id": 12, "box_id": 2},
    {"id": 3, "container_id": 3, "box_id": 23},
    {"id": 4, "container_id": 4, "box_id": 24},
    {"id": 5, "container_id": 5, "box_id": 2},
    {"id": 6, "container_id": 6, "box_id": 6},
    {"id": 7, "container_id": 7, "box_id": 7},
    {"id": 8, "container_id": 18, "box_id": 28},
    {"id": 9, "container_id": 19, "box_id": 29},
    {"id": 10, "container_id": 11, "box_id": 21},
]
with open("./freights.json", "w+") as file:
    file.write(json.dumps(freights))