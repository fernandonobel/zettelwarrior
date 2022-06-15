import datetime

from zettelwarrior.zettel import Zettel
from zettelwarrior.zettelkasten import Zettelkasten


def test_zettelkasten():

    zettelkasten = Zettelkasten("./examples/")

    expected = [Zettel().load("./examples/220612-1235.md")]

    assert zettelkasten.zettels == expected


def test_tags():

    zettelkasten = Zettelkasten("./examples/")
    result = zettelkasten.tags()
    expected = {"example-note": [None], "test": [None]}

    assert result == expected


def test_new_uuid():

    fake_now = datetime.datetime(2022, 6, 15, 20, 11, 55)
    zettelkasten = Zettelkasten("./examples/")
    result = zettelkasten.generate_new_uuid(fake_now)

    expected = "220615-2011"

    assert result == expected


def test_add_zettel(tmpdir):

    zettelkasten = Zettelkasten(str(tmpdir))
    filepath, uuid = zettelkasten.add_zettel()

    result = Zettel().load(filepath)

    expected = Zettel()
    expected.title = "None"
    expected.uuid = uuid
    expected.tags = []
    expected.status = None
    expected.backlink = None

    assert result == expected
