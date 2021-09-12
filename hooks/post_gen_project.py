import os


def on_open_source():
    pass


def on_private_project():
    pass


def sphinx_quickstart():
    pass


NEXT_STEPS = """
\033[1;32m  Next steps:  \033[1;m

cd {{cookiecutter.project_name}}

poetry install --no-root
{%- if cookiecutter.docs == 'y' %}
poetry run sphinx-quickstart --quiet -p '{{cookiecutter.project_title}}' -r '{{cookiecutter.version}}' -a '{{cookiecutter.full_name}}' --ext-doctest docs
{%- endif %}

git init
git add .
git commit -m "Init commit"

git remote add origin {{ cookiecutter.git_ssh }}
git push -u origin master
"""


def main():
    if '{{ cookiecutter.open_source }}' == 'y':
        on_open_source()
    else:
        on_private_project()

    print(NEXT_STEPS)


if __name__ == '__main__':
    main()
