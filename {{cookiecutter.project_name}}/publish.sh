#!/bin/bash

.githooks/pre-commit || exit 1

python3 setup.py bdist_wheel && twine upload dist/*; rm dist/*
