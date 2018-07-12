from pathlib import Path

from cookiecutter.main import cookiecutter

from pytest import fixture


@fixture(scope='session')
def project_title():
    return 'Project Title'


@fixture
def project_name(open_source, docs):
    name = 'project'

    if open_source == 'y':
        name += '-opensource'
    elif open_source == 'n':
        name += '-private'

    if docs == 'y':
        name += '-docs'
    elif docs == 'n':
        name += '-nodocs'

    return name


@fixture
def package_name(project_name):
    return project_name.replace('-', '_')


@fixture
def docs():
    return None


@fixture
def context(project_title, project_name, package_name, open_source, docs):
    context_ = {
        'project_title': project_title,
        'project_name': project_name,
        'package_name': package_name,
    }

    if open_source is not None:
        context_['open_source'] = open_source

    if docs is not None:
        context_['docs'] = docs

    return context_


@fixture
def project_path(tmpdir_factory, project_name, context):

    basetemp = tmpdir_factory.getbasetemp()
    project_dir = basetemp.join(project_name)

    if not project_dir.isdir():
        cookiecutter('.', output_dir=str(basetemp), no_input=True, extra_context=context)

    return Path(project_dir)


@fixture
def gitignore_content(project_path):
    with open(project_path / '.gitignore') as gitignore:
        yield gitignore.read()
