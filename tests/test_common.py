from pytest import fixture, mark


@fixture(params=['y', 'n'])
def open_source(request):
    return request.param


def test_common_files_existence(project_path, package_name):

    assert (project_path / package_name).is_dir()
    assert (project_path / 'tests').is_dir()

    assert (project_path / '.editorconfig').is_file()
    assert not (project_path / '.env').is_file()
    assert (project_path / '.gitignore').is_file()
    assert (project_path / 'Pipfile').is_file()
    assert (project_path / 'README.md').is_file()
    assert (project_path / 'setup.cfg').is_file()


def test_pytest(monkeypatch, project_path):
    """
    Run pytest in project dir
    """
    import pytest

    monkeypatch.syspath_prepend(project_path)

    assert pytest.main([project_path]) == 0
