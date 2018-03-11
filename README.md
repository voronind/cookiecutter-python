Python Project Template
=======================

Using
-----
```commandline
cookiecutter gh:dimka665/cookiecutter-python
```
Init project
```commandline
cd project
python -m venv .venv
pipenv shell
pipenv install --dev
git add .
git commit -m "Init commit"

git remote add origin git@github.com:user/project.git
git push -u origin master
```

Tests
-----
- Create virtual environment and activate it
- Install dependencies from `requirements.txt`
- Run `pytest`

```commandline
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
pytest
```
