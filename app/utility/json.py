import json
from pathlib import Path


def load_config(config_path: Path):

    '''returns the configuration data from a JSON file located at the specified path.'''

    with open(config_path, "r") as f:
        return json.load(f)


def save_config(config, config_path: Path):

    '''saves the configuration data to a JSON file located at the specified path.'''

    with open(config_path, "w") as f:
        json.dump(config, f, indent=4)