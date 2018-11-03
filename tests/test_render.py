import pathlib

from biohazard.core.render import render
from biohazard.core.io import load_yaml


def test_render():
    current_directory = pathlib.Path(__file__).parent

    expected_result = open(current_directory / 'test_render_result.html', 'r', encoding='utf-8').read()

    data = load_yaml(current_directory / 'test_render_data.yaml')

    result = render(data)

    assert result == expected_result, "Rendered result is not identical to expected result."
