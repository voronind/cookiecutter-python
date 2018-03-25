import pytest


def test_app_in_project_dir(project_path, package_name):
    assert (project_path / package_name).is_dir()


def test_pytest(monkeypatch, project_path):
    """
    Run pytest in project dir
    """
    monkeypatch.syspath_prepend(project_path)

    assert pytest.main([project_path]) == 0
