import pathlib
import yaml

from biohazard.core.exceptions import ContentDataException


def load_yaml(file: pathlib.Path) -> dict:
    """
    Reads the YAML file form the filesystem and parse it to a Python dictionary equivalent.

    :param file: location of the YAML file to read
    :return: dictionary equivalent of YAML file.
    """
    with open(file, 'r') as stream:
        data_loaded = yaml.load(stream)

    if type(data_loaded) is not dict:
        raise ContentDataException(f'Content of {file} was not parsed to a dictionary.')

    return data_loaded


def is_yaml(file):
    if load_yaml(file):
        return True
    return False


def get_contents(path: pathlib.Path) -> list:
    return [file for file in path.iterdir() if is_yaml(file)]
