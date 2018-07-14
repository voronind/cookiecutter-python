import json
from pathlib import Path

from setuptools import setup


def get_packages_from_pipfile_lock():

    with open(Path(__file__).parent / 'Pipfile.lock') as pipfile_lock:
        pipfile_lock_content = json.load(pipfile_lock)

    requirements = []
    for name, attrs in pipfile_lock_content['default'].items():
        requirements.append(name + attrs['version'])

    return requirements


setup(install_requires=get_packages_from_pipfile_lock())
