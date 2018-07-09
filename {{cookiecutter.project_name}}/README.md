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
git clone {{cookiecutter.git_repo}}
cd {{cookiecutter.project_name}}

pipenv install --dev
echo 'PYTHONPATH=.' > .env
```

Run tests:
```console
pipenv run pytest
```

Publish
-------
```console
python3 setup.py bdist_wheel
twine upload dist/*
rm dist/*
```

Deployment
----------
```console
pipenv install --system --deploy
```
