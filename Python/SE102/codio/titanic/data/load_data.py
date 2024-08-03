import json

FILE_PATH = "ships_data.json"


def load_data(file_path: str):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)
