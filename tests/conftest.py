import pytest


@pytest.fixture(scope='session')
def context():
    return {
        'project_title': 'Test Project',
        'dynamic_versioning': False,
        'pytest': False,
        'sphinx': False,

        'full_name': 'Full Name',
        'email': 'user@example.com',
        'git_hositng_user': 'user',
    }


@pytest.fixture(scope='module')
def project_path(cookies_session, context):
    result = cookies_session.bake(extra_context=context)
    assert result.exit_code == 0
    assert result.exception is None

    return result.project_path
