import shutil

from biohazard.conf.settings import assets_path, contents_path, output_path
from biohazard.core.io import get_contents, load_yaml
from biohazard.core.render import render


def collect_assets():
    """
    Collect all static assets from the assets directory if it exists.
    """
    if not assets_path.exists():
        raise Exception("Path does not exist.")

    shutil.copytree(assets_path, output_path)


def collect_contents():
    """
    Render all content and collect it.
    """
    files = get_contents(contents_path)

    for file in files:
        data = load_yaml(file)
        rendered_data = render(data)
        workfile = file.stem + '.html'
        with open(output_path / workfile, 'w') as stream:
            stream.write(rendered_data)
