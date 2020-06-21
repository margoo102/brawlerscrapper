import json

def read_json(file='example.json'):
    with open(file, 'r') as config_file:
        data = config_file.read()
        return json.loads(data)
