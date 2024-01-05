import contextlib
import os
import subprocess
import shutil

import tomlkit

NEXT_STEPS = """
\033[1;32m  Next steps:  \033[1;m

cd {{cookiecutter.project_name}}

git commit -m "Init commit"
git tag --annotate -m Version v0.1
git push -u origin master
"""

@contextlib.contextmanager
def edit_toml(file_path):
    with open(file_path) as pyproject_toml:
        doc = tomlkit.parse(pyproject_toml.read())

    yield doc

    with open(file_path, 'w') as pyproject_toml:
        tomlkit.dump(doc, pyproject_toml)


def lisense():
    if '{{ cookiecutter.license }}' == 'Proprietary':
        os.unlink('LICENSE')


def pytest():
    if '{{ cookiecutter.pytest }}' != 'y':
        os.unlink('pytest.ini')
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

def poetry_init():
    command = [
        'poetry',
        'init',
        '--no-interaction',
        '--description={{cookiecutter.project_description}}',
        '--license={{cookiecutter.license}}',
        '--author={{cookiecutter.full_name}} <{{cookiecutter.email}}>',
        '--dev-dependency=ipython',
    ]

    if '{{ cookiecutter.pytest }}' == 'y':
        command += [
            '--dev-dependency=pytest',
            '--dev-dependency=pytest-cov',
            # '--dev-dependency=pytest-pythonpath',
        ]
    if '{{ cookiecutter.sphinx }}' == 'y':
        command += [
            '--dev-dependency=sphinx',
            '--dev-dependency=sphinx-autobuild',
        ]

    subprocess.check_call(command)

    with edit_toml('pyproject.toml') as doc:
        doc['tool']['poetry']['homepage'] = "{{cookiecutter.__git_http}}"
        doc['tool']['poetry']['repository'] = "{{cookiecutter.__git_http}}"

        if '{{ cookiecutter.rtd }}' == 'y':
            doc['tool']['poetry']['documentation'] = "https://readthedocs.io"

        if '{{ cookiecutter.license }}' == 'Proprietary':
            classifiers = tomlkit.array()
            classifiers.add_line('Private :: Do Not Upload')
            classifiers.add_line(indent='')
            doc['tool']['poetry']['classifiers'] = classifiers


def git():
    subprocess.check_call(['git', 'init'])
    subprocess.check_call(['pre-commit', 'install'])
    # subprocess.check_call(['pre-commit', 'autoupdate'])
    subprocess.check_call(['git', 'add', '.'])
    subprocess.check_call(['git', 'remote', 'add', 'origin', '{{ cookiecutter.__git_ssh }}'])

def poetry_dynamic_versioning():
    if '{{ cookiecutter.poetry_dynamic_versioning }}' != 'y':
        return

    with edit_toml('pyproject.toml') as doc:
        doc['tool']['poetry']['version'] = '0'
        doc['tool'].append('poetry-dynamic-versioning', {
            'enable': True,
            'strict': True,
            'latest-tag': True,
        })
        doc['build-system']['requires'].append('poetry-dynamic-versioning>=1.0.0,<2.0.0')
        doc['build-system']['build-backend'] = 'poetry_dynamic_versioning.backend'


def main():
    lisense()
    pytest()
    sphinx_quickstart()
    poetry_init()
    if os.environ.get('TESTING') != '1':
        subprocess.check_call(['poetry', 'install', '--no-root'])
        git()
    poetry_dynamic_versioning()

    print(NEXT_STEPS)


if __name__ == '__main__':
    main()
