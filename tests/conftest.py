import os

from pytest import fixture


@fixture(scope='session', autouse=True)
def environment_variable():
    os.environ['TESTING'] = '1'


@fixture()
def project_path(cookies):
    extra_context = {
        'project_title': 'Project',

    }
    def _cookies_project_path(**context):
        result = cookies.bake(extra_context=dict(**extra_context, **context))
        assert result.exit_code == 0
        assert result.exception is None
        return result.project_path

    return _cookies_project_path
