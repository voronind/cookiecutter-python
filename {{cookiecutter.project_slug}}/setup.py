from setuptools import setup, find_packages

import json
from pathlib import Path


def get_install_requires():

    with open(Path(__file__).parent / 'Pipfile.lock') as pipfile_lock:
        pipfile_content = json.load(pipfile_lock)

    requirements = []
    for name, attrs in pipfile_content['default'].items():
        requirements.append(name + attrs['version'])

    return requirements


setup(
    name='{{cookiecutter.project_slug}}',
    version='{{cookiecutter.version}}',

    author='{{cookiecutter.full_name}}',
    author_email='{{cookiecutter.email}}',

    url='https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}',
    description={{cookiecutter.project_short_description.__repr__()}},

    packages=find_packages(),
    install_requires=get_install_requires(),

    license='MIT License',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    keywords='',
)
