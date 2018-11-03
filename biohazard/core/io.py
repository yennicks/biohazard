import pathlib
import yaml


def load_yaml(file: pathlib.Path):
    with open(file, 'r') as stream:
        data_loaded = yaml.load(stream)
    return data_loaded


def is_yaml(file):
    if load_yaml(file):
        return True
    return False


def get_contents(path: pathlib.Path) -> list:
    return [file for file in path.iterdir() if is_yaml(file)]
