import datetime
from distutils.dir_util import copy_tree
import filecmp
import os
from pathlib import Path

import pytest
from zettelwarrior.config import Config
from zettelwarrior.zettel import Zettel
from zettelwarrior.zettelkasten import Zettelkasten


@pytest.fixture
def tmp_zettelkasten_dir(tmpdir):
    result = Path(tmpdir)
    copy_example_files_into(result)
    return result


def copy_example_files_into(path):
    copy_tree("./examples/", str(path))


def test_zettelkasten(tmp_zettelkasten_dir):
    config = Config()
    config.path = Path(tmp_zettelkasten_dir)
    zettelkasten = Zettelkasten(config)
    result = zettelkasten.zettels

    expected = [Zettel().load("./examples/220612-1235.md")]

    assert result == expected


def test_tags():

    config = Config()
    config.load_config_file("./examples/.zwrc")

    zettelkasten = Zettelkasten(config)
    result = zettelkasten.tags()

    expected = {
        "example-note": [Zettel().load("./examples/220612-1235.md")],
        "test": [Zettel().load("./examples/220612-1235.md")],
    }

    assert result == expected


def test_generate_tag_index(tmp_zettelkasten_dir):

    os.remove(tmp_zettelkasten_dir / "tags.md")

    config = Config()
    config.path = Path(tmp_zettelkasten_dir)

    zettelkasten = Zettelkasten(config)
    zettelkasten.generate_tag_index()

    result = str(tmp_zettelkasten_dir / "tags.md")
    expected = "./examples/tags.md"

    assert filecmp.cmp(result, expected)


def test_new_uuid():

    fake_now = datetime.datetime(2022, 6, 15, 20, 11, 55)

    config = Config()
    config.load_config_file("./examples/.zwrc")

    zettelkasten = Zettelkasten(config)
    result = zettelkasten.generate_new_uuid(fake_now)
    expected = "220615-2011"
    assert result == expected


def test_add_zettel(tmpdir):

    config = Config()
    config.path = Path(tmpdir)

    zettelkasten = Zettelkasten(config)
    filepath, uuid = zettelkasten.add_zettel()
    result = Zettel().load(filepath)

    expected = Zettel()
    expected.title = "None"
    expected.uuid = uuid
    expected.tags = []
    expected.status = None
    expected.backlink = None

    assert result == expected


def test_generate_multiple_uuid_at_same_time(tmpdir):

    config = Config()
    config.path = Path(tmpdir)

    fake_now = datetime.datetime(2022, 6, 15, 20, 11, 55)

    zettelkasten = Zettelkasten(config)

    result = []

    filepath, uuid = zettelkasten.add_zettel(None, fake_now)
    result.append(uuid)

    filepath, uuid = zettelkasten.add_zettel(None, fake_now)
    result.append(uuid)

    filepath, uuid = zettelkasten.add_zettel(None, fake_now)
    result.append(uuid)

    expected = []
    expected.append("220615-2011")
    expected.append("220615-2011a")
    expected.append("220615-2011b")

    assert result == expected
