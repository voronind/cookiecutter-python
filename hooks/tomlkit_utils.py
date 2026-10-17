import contextlib
from pathlib import Path

import tomlkit


def _toml_mapping_key_index(
    toml_mapping: tomlkit.TOMLDocument | tomlkit.items.AbstractTable,
    keys: list[str],
):
    toml_mapping_keys = list(toml_mapping.keys())
    for key in keys:
        if key in toml_mapping_keys:
            return toml_mapping_keys.index(key)
    raise LookupError


def toml_insert_after_key(
    toml_mapping: tomlkit.TOMLDocument | tomlkit.items.AbstractTable,
    keys: list[str],
    toml_item: (tomlkit.items.Key, tomlkit.items.Item),
):
    if isinstance(toml_mapping, tomlkit.TOMLDocument):  # ruff:ignore[if-else-block-instead-of-if-exp]
        body = toml_mapping.body
    else:
        body = toml_mapping._value.body    # ruff:ignore[private-member-access]

    index = _toml_mapping_key_index(toml_mapping, keys)
    body.insert(index + 1, toml_item)


def toml_replace_key(
    table: tomlkit.items.AbstractTable,
    key: str,
    item: (tomlkit.items.Key, tomlkit.items.Item),
):
    index = _toml_mapping_key_index(table, [key])
    table._value.body[index] = item         # ruff:ignore[private-member-access]


@contextlib.contextmanager
def edit_toml(file_path):
    with Path(file_path).open() as toml_file:
        doc = tomlkit.parse(toml_file.read())

    yield doc

    with Path(file_path).open('w') as toml_file:
        tomlkit.dump(doc, toml_file)
