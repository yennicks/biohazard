import pathlib
import shutil

from biohazard.conf.settings import output_path
from biohazard.core.io import get_contents, load_yaml
from biohazard.core.render import render


def collect_assets():
    assets_path = pathlib.Path('assets')
    if not assets_path.exists():
        raise Exception("Path does not exist.")

    shutil.copytree(assets_path, output_path)


def collect_contents():
    contents_dir = pathlib.Path('contents')
    files = get_contents(contents_dir)
    for file in files:
        data = load_yaml(file)
        rendered_data = render(data)
        workfile = file.stem + '.html'
        with open(output_path / workfile, 'w') as stream:
            stream.write(rendered_data)

    # gitignore
    # ready for v0.0
    # upload to gitlab
    # register domain
    # v0.1 proper testing, documentation
