{{cookiecutter.project_title}}
=============================

{{cookiecutter.project_description}}

Development
-----------
We need installed `pyenv` and `pipenv`.
```commandline
git clone {{cookiecutter.git_repo}}
cd {{cookiecutter.project_name}}
python -m venv .venv
echo 'PYTHONPATH=.' > .env
pipenv install --dev
pipenv shell
```

When `pipenv` will use `pyenv` to install Python versions
and generate short virtual environment names we will not
create virtual environment manually.

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
