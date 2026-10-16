import json
from pathlib import Path
from utility.path import get_project_root


def load_config(config_path: Path):

    '''returns the configuration data from a JSON file located at the specified path.'''

    with open(config_path, "r") as f:
        return json.load(f)


def save_config(config, config_path: Path):

    '''saves the configuration data to a JSON file located at the specified path.'''

    with open(config_path, "w") as f:
        json.dump(config, f, indent=4)


def update_device_config(name,key,value):
    
    data = load_config(get_project_root('main')/'config'/'deviceconfig.json')

    for device in data["devices"]:

        if device["name"] == name:
            device[key] = value

    save_config(data, get_project_root('main')/'config'/'deviceconfig.json')