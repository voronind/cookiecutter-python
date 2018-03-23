from pathlib import Path

from pytest import fixture


@fixture(scope='session')
def project_title():
    return 'Charged Project'


@fixture(scope='session')
def project_name(project_title):
    return project_title.lower().replace(' ', '-')


@fixture(scope='session')
def package_name(project_name):
    return project_name.replace('-', '_')


@fixture(scope='session')
def extra_context(project_title):
    return {'project_title': project_title}


@fixture(scope='session')
def output_dir(tmpdir_factory):
    return tmpdir_factory.mktemp('cookiecutter', numbered=False)


@fixture(scope='session')
def project_path(output_dir, project_name):
    return Path(output_dir, project_name)


@fixture(scope='session', autouse=True)
def render_project(output_dir, extra_context):
    from cookiecutter.main import cookiecutter

    cookiecutter('.', output_dir=output_dir, no_input=True, extra_context=extra_context)
