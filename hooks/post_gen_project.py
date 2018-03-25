import os


def on_open_source():
    pass


def on_private():
    os.remove('LICENSE')


if __name__ == '__main__':
    if '{{ cookiecutter.open_source }}' == 'y':
        on_open_source()
    else:
        on_private()
