import re
import sys

project_name = "{{ cookiecutter.project_name }}"

if not re.match(r'^[a-z][a-z\d-]+$', project_name):
    print(f'ERROR: The project name {project_name!r} is invalid.')
    sys.exit(1)
