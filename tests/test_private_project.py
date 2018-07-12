from pytest import fixture


@fixture
def open_source():
    return 'n'


def test_specific_files(project_path):
    assert not (project_path / 'LICENSE').is_file()
    assert not (project_path / 'setup.py').is_file()


def test_gitignore(gitignore_content):
    assert 'Pipfile.lock' not in gitignore_content
