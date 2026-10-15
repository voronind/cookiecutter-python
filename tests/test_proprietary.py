

def test_proprietary_license(min_project_path):
    path = min_project_path(license='Proprietary')

    assert not (path / 'LICENSE').is_file()
