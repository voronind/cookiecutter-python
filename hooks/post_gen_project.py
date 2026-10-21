import shutil
import subprocess
from pathlib import Path

"""
Why `tomlkit` is shit.

1. Can not insert random keys (e.g. `dependency-groups`)
   between `project` and `project.scripts` document root keys.
2. Two different dotted keys with common part creates additional upper-level key.
3. Hard to add spaces.
"""


def line_index(lines, target_line):
    for index, line in enumerate(lines):
        if line.startswith(target_line):
            return index
    raise LookupError(target_line)


def insert_after_line(lines, target_line: str, insert_lines: list[str]):
    index = line_index(lines, target_line) + 1
    lines[index:index] = insert_lines


def insert_before_line(lines, target_line, insert_lines):
    index = line_index(lines, target_line)
    lines[index:index] = insert_lines


def replace_line(lines, target_line, insert_lines):
    index = line_index(lines, target_line)
    lines[index:index + 1] = insert_lines


def read_pyproject_lines():
    with Path('pyproject.toml').open('r') as file:
        return file.readlines()


def write_pyproject_lines(lines):
    with Path('pyproject.toml').open('w') as file:
        file.writelines(lines)


def lisense():
    if '{{ cookiecutter.license }}' == 'Proprietary':
        Path('LICENSE').unlink()


def pytest():
    if '{{ cookiecutter.pytest }}' != 'y':
        Path('pytest.ini').unlink()
        Path('.coveragerc').unlink()
        shutil.rmtree('tests')


def sphinx_quickstart():
    if '{{ cookiecutter.sphinx }}' != 'y':
        return

    subprocess.check_call([
        'uv',
        'run',
        'sphinx-quickstart',
        '--quiet',
        '--project',
        '{{ cookiecutter.project_title }}',
        '--author',
        '{{ cookiecutter.full_name }}',
        '--extensions',
        'autobuild',
        'docs',
    ])

    # Git doesn't like CRLF line terminators
    Path('docs/make.bat').unlink()


def uv_init():
    uv_init_command = [
        'uv',
        'init',
        '--name',
        '{{cookiecutter.project_name}}',
        '--description',
        '{{cookiecutter.description}}',
    ]
    if '{{ cookiecutter.dynamic_versioning }}' == 'y':
        uv_init_command += ['--build-backend', 'hatch']

    subprocess.check_call(uv_init_command)
    shutil.rmtree('src')

    lines = read_pyproject_lines()

    project_urls = [
        'urls.repository = "{{cookiecutter.__git_http}}"\n',
    ]

    if '{{ cookiecutter.rtd }}' == 'y':
        project_urls.append('urls.documentation = "https://{{cookiecutter.project_name}}.readthedocs.org"\n')

    insert_before_line(
        lines,
        'requires-python = ',
        project_urls,
    )

    insert_after_line(
        lines,
        'dependencies = []',
        ['\n', '[dependency-groups]\n', '\n'],
    )

    if '{{ cookiecutter.license }}' == 'Proprietary':
        classifiers = [
            'classifiers = [\n',
            '    "Private :: Do Not Upload",\n',
            ']\n',
        ]
        insert_before_line(lines, 'requires-python = ', classifiers)

    lines += ['\n']

    if '{{ cookiecutter.dynamic_versioning }}' == 'y':
        dynamic_versioning(lines)
    else:
        lines += [
            '[tool.uv.build-backend]\n',
            'module-root = ""\n',
            '\n',
        ]

    lines += [
        '[tool.uv]\n',
        'preview-features = ["centralized-project-envs"]\n',
        '\n',
    ]

    write_pyproject_lines(lines)

    if '{{ cookiecutter.pytest }}' == 'y':
        subprocess.check_call(['uv', 'add', '--dev', 'pytest', 'pytest-cov', 'pytest-xdist'])

    if '{{ cookiecutter.sphinx }}' == 'y':
        subprocess.check_call(['uv', 'add', '--dev', 'sphinx', 'sphinx-autobuild'])


def dynamic_versioning(lines):
    if '{{ cookiecutter.dynamic_versioning }}' != 'y':
        return

    replace_line(
        lines,
        'version = ',
        ['dynamic = ["version"]\n'],
    )

    replace_line(
        lines,
        'requires = ["hatchling"]',
        ['requires = ["hatchling", "hatch-vcs"]\n'],
    )

    lines += [
        '[tool.hatch.version]\n',
        'source = "vcs"\n',
        'raw-options = { local_scheme = "no-local-version" }\n',
        '\n',
        '[tool.hatch.build.targets.sdist]\n',
        'include = [\n',
        '    "{{ cookiecutter.__package_name }}",\n',
        '    "README.md",\n',
        ']\n',
        '\n',
    ]


def git_init():
    subprocess.check_call(['git', 'init'])
    subprocess.check_call(['git', 'config', 'user.name', '{{ cookiecutter.full_name }}'])
    subprocess.check_call(['git', 'config', 'user.email', '{{ cookiecutter.email }}'])
    # при отправке ветки отправляются и тэги, которые в ней находятся.
    subprocess.check_call(['git', 'config', 'push.followTags', 'true'])
    # перед получением списка веток с сервера сначала удаляются локальные копии веток, которых на сервере больше нет.
    subprocess.check_call(['git', 'config', 'fetch.prune', 'true'])
    # мержить только фaст-форвардом
    subprocess.check_call(['git', 'config', 'merge.ff', 'only'])

    subprocess.check_call(['pre-commit', 'install'])
    subprocess.check_call(['git', 'remote', 'add', 'origin', '{{ cookiecutter.__git_ssh }}'])


def git_hosting():
    if '{{ cookiecutter.git_hosting }}' != 'github.com':
        shutil.rmtree('.github')


def print_next_commands():
    # Add pre-commit autoupdate
    next_commands = """
    \033[1;32m  Next steps:  \033[1;m

cd {{cookiecutter.project_name}}

pre-commit autoupdate
{% if cookiecutter.git_hosting == 'github.com' -%}
update-gha

{% endif -%}

git add .
git commit -m "Init commit"

git tag --annotate -m Version v0.1

git push --set-upstream origin main
    """
    print(next_commands)    # ruff:ignore[print]


def main():
    lisense()
    pytest()
    uv_init()
    sphinx_quickstart()
    git_init()
    git_hosting()
    print_next_commands()


if __name__ == '__main__':
    main()
