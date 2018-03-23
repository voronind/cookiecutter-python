import re
import sys


project_name = "{{ cookiecutter.project_name }}"

if not re.match(r'^[a-z][a-z\d-]+$', project_name):
    print(f'ERROR: The project name {project_name!r} is invalid.')

    # Exit to cancel project
    sys.exit(1)


package_name = "{{ cookiecutter.package_name }}"

if not re.match(r'^[a-z][a-z\d_]+$', package_name):
    print(f'ERROR: The package name {package_name!r} is invalid.')

    # Exit to cancel project
    sys.exit(1)
