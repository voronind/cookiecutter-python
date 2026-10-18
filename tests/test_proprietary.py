import pytest


@pytest.fixture(scope='module')
def context(context):
    return context | {'license': 'Proprietary'}


def test_proprietary_license(project_path):
    assert not (project_path / 'LICENSE').is_file()
