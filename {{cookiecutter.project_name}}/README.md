{{cookiecutter.project_title}}
=============================

{{cookiecutter.project_description}}

Install
-------
```commandline
pip install {{cookiecutter.package_name}}
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
pipenv run test
```
