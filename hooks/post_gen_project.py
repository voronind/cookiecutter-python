import os


def on_open_source():
    pass


def on_private():
    os.remove('LICENSE')


NEXT_STEPS = """
\033[1;32m  Next steps:  \033[1;m

cd {{cookiecutter.project_name}}

pipenv install --dev

git init
git add .
git commit -m "Init commit"

git remote add origin {{cookiecutter.git_repo}}
git push -u origin master
"""


def main():
    if '{{ cookiecutter.open_source }}' == 'y':
        on_open_source()
    else:
        on_private()

    print(NEXT_STEPS)


if __name__ == '__main__':
    main()
