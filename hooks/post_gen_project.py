import contextlib
import shutil
import subprocess
from pathlib import Path

import tomlkit


def _toml_table_key_index(
    table: tomlkit.items.AbstractTable,
    keys: list[str],
):
    table_keys = list(table.keys())
    for key in keys:
        if key in table_keys:
            return table_keys.index(key)
    raise LookupError


def insert_in_toml_table_after_key(
    table: tomlkit.items.AbstractTable,
    keys: list[str],
    item: (tomlkit.items.Key, tomlkit.items.Item),
):
    index = _toml_table_key_index(table, keys)
    table._value.body.insert(index + 1, item)       # ruff:ignore[private-member-access]


def replace_toml_table_key(
    table: tomlkit.items.AbstractTable,
    key: str,
    item: (tomlkit.items.Key, tomlkit.items.Item),
):
    index = _toml_table_key_index(table, [key])
    table._value.body[index] = item         # ruff:ignore[private-member-access]


@contextlib.contextmanager
def edit_toml(file_path):
    with Path(file_path).open() as toml_file:
        doc = tomlkit.parse(toml_file.read())

    yield doc

    with Path(file_path).open('w') as toml_file:
        tomlkit.dump(doc, toml_file)


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
        'sphinx-quickstart',
        '--quiet',
        '-p',
        '{{cookiecutter.project_title}}',
        '-a',
        '{{cookiecutter.full_name}}',
        '--ext-doctest',
        'docs',
    ])


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

    if '{{ cookiecutter.pytest }}' == 'y':
        subprocess.check_call(['uv', 'add', '--dev', 'pytest', 'pytest-cov', 'pytest-xdist'])

    if '{{ cookiecutter.sphinx }}' == 'y':
        subprocess.check_call(['uv', 'add', '--dev', 'sphinx', 'sphinx-autobuild'])

    project_urls = {
        'repository': '{{cookiecutter.__git_http}}',
    }

    if '{{ cookiecutter.rtd }}' == 'y':
        project_urls['documentation'] = 'https://{{cookiecutter.project_name}}.readthedocs.org'

    with edit_toml('pyproject.toml') as doc:
        doc['project']['urls'] = project_urls
        doc['project']['urls'].add(None, tomlkit.ws('\n'))

        if '{{ cookiecutter.license }}' == 'Proprietary':
            classifiers = tomlkit.array()
            classifiers.add_line('Private :: Do Not Upload')
            classifiers.add_line(indent='')

            insert_in_toml_table_after_key(
                doc['project'],
                ['authors'],
                (tomlkit.key('classifiers'), classifiers),
            )

        if '{{ cookiecutter.dynamic_versioning }}' != 'y':
            if 'tool' not in doc:
                doc['tool'] = {}

            if 'uv' not in doc['tool']:
                doc['tool']['uv'] = {}

            doc['tool']['uv']['build-backend'] = {
                'module-root': '.',
            }


def dynamic_versioning():
    if '{{ cookiecutter.dynamic_versioning }}' != 'y':
        return

    with edit_toml('pyproject.toml') as doc:
        replace_toml_table_key(
            doc['project'],
            'version',
            (tomlkit.key('dynamic'), tomlkit.array('["version"]')),
        )

        doc['build-system']['requires'].append('hatch-vcs')

        hatch_version_raw_options = tomlkit.inline_table()
        hatch_version_raw_options['local_scheme'] = 'no-local-version'
        hatch_version_raw_options['local_scheme'].trivia.indent = ' '
        hatch_version_raw_options['local_scheme'].trivia.trail = ' '

        if 'tool' not in doc:
            doc['tool'] = {}
        doc['tool']['hatch'] = {
                'version': {
                    'source': 'vcs',
                    'raw-options': hatch_version_raw_options,
                },
        }

        dist_include = tomlkit.array()
        dist_include.multiline(True)
        dist_include.append('{{cookiecutter.__package_name}}')
        dist_include.append('README.md')

        doc['tool']['hatch']['build'] = {
            'targets': {
                'sdist': {
                    'include': dist_include,
                },
            },
        }


def git_init():
    subprocess.check_call(['git', 'init'])
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
    sphinx_quickstart()
    uv_init()
    dynamic_versioning()
    git_init()
    git_hosting()
    print_next_commands()


if __name__ == '__main__':
    main()
