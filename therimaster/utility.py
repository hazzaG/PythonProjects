import json

def read(path):
    with open(path, "r") as file:
        return file.read()

def read_json(path):
    return json.loads(read(path))

freq_map = read_json("freq_map.json")