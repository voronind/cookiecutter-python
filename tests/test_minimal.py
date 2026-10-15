from collections.abc import Callable
from pathlib import Path


def test_minimal_project(min_project_path: Callable[[], Path]):
    path = min_project_path()

    project_dir_content = {file.name for file in path.iterdir()}
    assert project_dir_content == {
        '.pylintrc',
        'LICENSE',
        '.editorconfig',
        'pyproject.toml',
        '.envrc',
        '.pre-commit-config.yaml',
        '.git',
        '.gitignore',
        '.flake8',
        'test_project',
        '.python-version',
        'README.md',
    }
