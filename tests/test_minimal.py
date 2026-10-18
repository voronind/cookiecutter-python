import subprocess


def test_minimal_project(project_path):
    project_dir_content = {file.name for file in project_path.iterdir()}
    assert project_dir_content == {
        '.github',
        'ruff.toml',
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


def test_pre_commit(project_path):
    validate_config_command = ['pre-commit', 'validate-config', project_path / '.pre-commit-config.yaml']
    assert subprocess.check_call(validate_config_command) == 0
