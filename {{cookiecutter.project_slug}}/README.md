{{cookiecutter.project_name}}
=============================

{{cookiecutter.project_short_description}}

Development
-----------
We need installed `pyenv` and `pipenv`.
```commandline
pipenv install --dev
```

If this doesn't work try:
```commandline
pyenv install 3.6.4
pyenv shell 3.6.4
python -m venv .venv
pipenv install --dev
pipenv shell
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
