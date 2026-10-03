import json

def get_data(file):
    with open(file) as f:
        return json.load(f)