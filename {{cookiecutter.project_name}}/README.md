{{cookiecutter.project_title}}
=============================

{%- if cookiecutter.open_source == 'y' %}
[![PyPI](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_name }}.svg)](https://pypi.org/project/{{ cookiecutter.project_name }}/ "Latest version on PyPI")
[![Travis](https://travis-ci.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}.svg?branch=master)](https://travis-ci.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }} "Travis CI")
[![Docs](https://readthedocs.org/projects/{{ cookiecutter.project_name }}/badge/?version=stable)](https://{{ cookiecutter.project_name }}.readthedocs.io/en/latest/ "Read the docs")
[![codecov](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}/branch/master/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }} "Coverage")
{%- endif %}

{{ cookiecutter.project_description }}

Install
-------
```commandline
pip install {{ cookiecutter.package_name }}
```

Development
-----------
We need installed `pyenv` and `pipenv`.
```console
git clone {{ cookiecutter.git_ssh }}

cd {{ cookiecutter.project_name }}
pipenv install --dev
```

Run tests:
```console
pipenv run fulltest
```
