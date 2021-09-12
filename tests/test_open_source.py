import re

from pytest import fixture, mark


@fixture
def open_source():
    return 'y'


@mark.parametrize('open_source', [None, 'y'])
def test_specific_files(project_path):
    pass
