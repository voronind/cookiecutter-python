import re
import sys


project_name = "{{ cookiecutter.project_name }}"

if not re.match(r'^[a-z][a-z\d-]+$', project_name):
    print('ERROR: The project name {project_name!r} is invalid.'.format(project_name=project_name))

    # Exit to cancel project
    sys.exit(1)


package_name = "{{ cookiecutter.package_name }}"

if not re.match(r'^[a-z][a-z\d_]+$', package_name):
    print('ERROR: The package name {package_name!r} is invalid.'.format(package_name=package_name))

    # Exit to cancel project
    sys.exit(1)
