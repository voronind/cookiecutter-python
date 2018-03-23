import os


if '{{ cookiecutter.license }}' == 'Not open source':
    os.remove('LICENSE')
