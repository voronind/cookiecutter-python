import re
import sys


{% set git_hosting = ('bitbucket.org', 'github.com')[cookiecutter.open_source == 'y'] %}
{% set git_username = (cookiecutter.bitbucket_username, cookiecutter.github_username)[cookiecutter.open_source == 'y'] %}

{% set git_ssh  -%}     git@{{ git_hosting }}:{{ git_username }}/{{ cookiecutter.project_name }}.git {%- endset %}
{% set git_http -%} https://{{ git_hosting }}/{{ git_username }}/{{ cookiecutter.project_name }}     {%- endset %}

{% set x = cookiecutter.__setitem__('git_ssh', git_ssh) %}
{% set x = cookiecutter.__setitem__('git_http', git_http) %}


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
