
from {{cookiecutter.package_name}}.main import add


def test_main():
    assert add(2, 2) == 4
