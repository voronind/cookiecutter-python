import pytest


@pytest.fixture
def project_path(cookies):

    def _project_path(**context):
        result = cookies.bake(extra_context=context)
        assert result.exit_code == 0
        assert result.exception is None
        return result.project_path

    return _project_path


MIN_CONTEXT = {
    'project_title': 'Test Project',
    'dynamic_versioning': False,
    'pytest': False,
    'sphinx': False,

    'full_name': 'Full Name',
    'email': 'user@example.com',
    'git_hositng_user': 'user',
}


@pytest.fixture
def min_project_path(project_path):

    def _min_project_path(**context):
        return project_path(**(MIN_CONTEXT | context))

    return _min_project_path
