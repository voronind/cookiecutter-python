import subprocess

import pytest


@pytest.fixture(scope='module')
def context(context):
    return context | {'git_hosting': 'gitlab.com'}


def test_pre_commit(project_path):
    validate_config_command = ['pre-commit', 'validate-config', project_path / '.pre-commit-config.yaml']
    assert subprocess.check_call(validate_config_command) == 0
