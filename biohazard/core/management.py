import shutil

from biohazard.conf.settings import output_path
from biohazard.core.collector import collect_assets, collect_contents


def clean():
    shutil.rmtree(output_path)


def collect():
    collect_assets()
    collect_contents()


def run():
    clean()
    collect()
