import os
# from pathlib import Path
#
#
# PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
#
#
# def remove_file(filepath):
#     os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if '{{ cookiecutter.license }}' == 'Not open source':
    os.remove('LICENSE')
