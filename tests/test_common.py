from pytest import fixture, mark


def test_mit_license(project_path):
    path = project_path()

    assert (path / 'LICENSE').is_file()

    # assert (project_path / 'tests').is_dir()
    # assert (project_path / '.editorconfig').is_file()
    # assert (project_path / '.envrc').is_file()
    # assert (project_path / '.gitignore').is_file()
    # assert (project_path / 'README.md').is_file()


def test_proprietary_license(project_path):
    path = project_path(license='Proprietary')

    assert not (path / 'LICENSE').is_file()
