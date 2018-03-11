{{cookiecutter.project_name}}
=============================

{{cookiecutter.project_short_description}}

Development
-----------
We need installed `pyenv` and `pipenv`.
```commandline
pyenv install 3.6.4
pyenv shell 3.6.4
python -m venv .venv
pipenv shell
pipenv install --dev
```

When `pipenv` will use `pyenv` to install Python versions
and generate short virtual environment names we will prompt:
```commandline
pipenv shell
pipenv install --dev
```

Tests
-----
```commandline
pytest
```

Deployment
----------
```commandline
pipenv install --system --deploy
```
