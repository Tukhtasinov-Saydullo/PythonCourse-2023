import json

computers = [
    {
        'id': 1,
        'name': 'Asus',
        'color': 'black'
    },
    {
        'id': 2,
        'name': 'Omen',
        'color': 'black'
    },
    {
        'id': 3,
        'name': 'HP',
        'color': 'black'
    },
    {
        'id': 4,
        'name': 'Lenova',
        'color': 'black'
    }
]
with open('computers.json', 'w', newline='\n') as f:
    json.dump(computers, f)
