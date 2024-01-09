{{cookiecutter.project_title}}
=============================

{%- if cookiecutter.license != 'Proprietary' %}
[![PyPI](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_name }}.svg)](https://pypi.org/project/{{ cookiecutter.project_name }}/ "Latest version on PyPI")
{%- endif %}
{%- if cookiecutter.rtd == 'y' %}
[![Docs](https://readthedocs.org/projects/{{ cookiecutter.project_name }}/badge/?version=stable)](https://{{ cookiecutter.project_name }}.readthedocs.io/en/latest/ "Read the docs")
{%- endif %}
{%- if cookiecutter.codecov == 'y' %}
[![codecov](https://codecov.io/gh/{{ cookiecutter.git_user }}/{{ cookiecutter.project_name }}/branch/master/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.git_user }}/{{ cookiecutter.project_name }} "Coverage")
{%- endif %}

{{ cookiecutter.project_description }}

Install
-------
```commandline
pip install {{ cookiecutter.project_name }}
```

Development
-----------
We need installed `poetry`.
```console
git clone {{ cookiecutter.__git_ssh }}

cd {{ cookiecutter.project_name }}
poetry install --no-root
```

Run tests:
```console
poetry run pytest
```
