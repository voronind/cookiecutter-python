from pathlib import Path
from setuptools import setup

{% if cookiecutter.install_requires_from == 'Pipfile' %}
def get_packages_from_Pipfile():
    import toml

    with open(Path(__file__).parent / 'Pipfile') as pipfile:
        pipfile_content = toml.load(pipfile)

    requirements = []
    for name, version in pipfile_content['packages'].items():
        if version == '*':
            requirements.append(name)
        else:
            requirements.append(name + version)

    return requirements


setup(install_requires=get_packages_from_Pipfile()){% elif cookiecutter.install_requires_from == 'Pipfile.lock' %}
def get_packages_from_Pipfile_lock():
    import json

    with open(Path(__file__).parent / 'Pipfile.lock') as pipfile_lock:
        pipfile_lock_content = json.load(pipfile_lock)

    requirements = []
    for name, attrs in pipfile_lock_content['default'].items():
        requirements.append(name + attrs['version'])

    return requirements


setup(install_requires=get_packages_from_Pipfile_lock()){% endif %}
