from pathlib import Path

from setuptools import setup

import toml


def get_packages_from_Pipfile():

    with open(str(Path(__file__).parent / 'Pipfile')) as pipfile:
        pipfile_content = toml.load(pipfile)

    requirements = []
    for name, version in pipfile_content['packages'].items():
        if version == '*':
            requirements.append(name)
        else:
            requirements.append(name + version)

    return requirements


setup(install_requires=get_packages_from_Pipfile())
