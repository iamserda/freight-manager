import json # [missing-module-docstring]


records = [
    {
        "name": "Arya Stark",
        "weight": 12,
        "width": 4,
        "length": 3,
        "height": 2
    },
    {
        "name": "Jon Snow",
        "weight": 14,
        "width": 5,
        "length": 4,
        "height": 3
    },
    {
        "name": "Daenerys Targaryen",
        "weight": 10,
        "width": 3,
        "length": 2,
        "height": 1
    },
    {
        "name": "Tyrion Lannister",
        "weight": 8,
        "width": 2,
        "length": 2,
        "height": 2
    },
    {
        "name": "Cersei Lannister",
        "weight": 11,
        "width": 3,
        "length": 2,
        "height": 2
    },
    {
        "name": "Sansa Stark",
        "weight": 13,
        "width": 4,
        "length": 3,
        "height": 2
    },
    {
        "name": "Bran Stark",
        "weight": 9,
        "width": 3,
        "length": 2,
        "height": 1
    },
    {
        "name": "Jaime Lannister",
        "weight": 15,
        "width": 5,
        "length": 4,
        "height": 3
    },
    {
        "name": "Samwell Tarly",
        "weight": 18,
        "width": 6,
        "length": 4,
        "height": 3
    },
    {
        "name": "Jorah Mormont",
        "weight": 12,
        "width": 4,
        "length": 3,
        "height": 2
    },
    {
        "name": "Theon Greyjoy",
        "weight": 11,
        "width": 4,
        "length": 3,
        "height": 2
    },
    {
        "name": "Brienne of Tarth",
        "weight": 16,
        "width": 5,
        "length": 4,
        "height": 3
    },
    {
        "name": "Sandor Clegane",
        "weight": 17,
        "width": 6,
        "length": 5,
        "height": 4
    },
    {
        "name": "Petyr Baelish",
        "weight": 10,
        "width": 3,
        "length": 2,
        "height": 2
    },
    {
        "name": "Varys",
        "weight": 12,
        "width": 4,
        "length": 3,
        "height": 2
    },
    {
        "name": "Melisandre",
        "weight": 9,
        "width": 3,
        "length": 2,
        "height": 1
    },
    {
        "name": "Bronn",
        "weight": 13,
        "width": 4,
        "length": 3,
        "height": 2
    },
    {
        "name": "Gendry",
        "weight": 14,
        "width": 4,
        "length": 3,
        "height": 2
    },
    {
        "name": "Davos Seaworth",
        "weight": 12,
        "width": 4,
        "length": 3,
        "height": 2
    },
    {
        "name": "Tormund Giantsbane",
        "weight": 18,
        "width": 6,
        "length": 5,
        "height": 4
    },
    {
        "name": "Ygritte",
        "weight": 10,
        "width": 3,
        "length": 2,
        "height": 2
    },
    {
        "name": "Missandei",
        "weight": 8,
        "width": 3,
        "length": 2,
        "height": 2
    },
    {
        "name": "Grey Worm",
        "weight": 13,
        "width": 4,
        "length": 3,
        "height": 2
    },
    {
        "name": "Margaery Tyrell",
        "weight": 9,
        "width": 3,
        "length": 2,
        "height": 2
    },
    {
        "name": "Olenna Tyrell",
        "weight": 11,
        "width": 3,
        "length": 2,
        "height": 2
    }
]
json_records = json.dumps(records, indent=4)
