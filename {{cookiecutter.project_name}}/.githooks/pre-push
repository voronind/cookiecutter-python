#!/bin/bash

set -o errexit

pipenv run test
{%- if cookiecutter.docs == 'y' %}
pipenv run doctest
pipenv run build-docs
{%- endif %}

echo -e "\033[1;32m  Tests passed  \033[1;m"
