from pathlib import Path
from setuptools import setup

{% if cookiecutter.open_source == 'y' %}
def get_packages_from_Pipfile():
    from pipenv.project import Project
    from pipenv.utils import convert_deps_to_pip

    project = Project(chdir=False)
    pipfile = project.parsed_pipfile
    return convert_deps_to_pip(pipfile['packages'], r=False)


setup(install_requires=get_packages_from_Pipfile())

{%- else %}
def get_packages_from_Pipfile_lock():
    import json

    with open(Path(__file__).parent / 'Pipfile.lock') as pipfile_lock:
        pipfile_lock_content = json.load(pipfile_lock)

    requirements = []
    for name, attrs in pipfile_lock_content['default'].items():
        requirements.append(name + attrs['version'])

    return requirements


setup(install_requires=get_packages_from_Pipfile_lock())
{%- endif %}
