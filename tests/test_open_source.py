import re

from pytest import fixture, mark


@fixture
def open_source():
    return 'y'


@mark.parametrize('open_source', [None, 'y'])
def test_specific_files(project_path):
    assert (project_path / 'LICENSE').is_file()
    assert (project_path / 'setup.py').is_file()


def test_gitignore(gitignore_content):
    # Not empty line before.
    # Empty line after.
    assert re.search('\S\n/Pipfile\.lock\n\n\S', gitignore_content)
