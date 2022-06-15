from zettelwarrior.zettel import Zettel


def test_zettel():

    zettel = Zettel()

    assert isinstance(zettel, Zettel)


def test_load_zettel():

    zettel = Zettel()
    zettel.load("./examples/220612-1235.md")

    assert zettel.title == "This is the title of the example note."
    assert zettel.uuid == "220612-1235"
    assert zettel.tags == ["example-note", "test"]
    assert zettel.status == "done"
    assert zettel.backlink == "<[La metodología Zettelkasten](220610-1709)>"


def test_zettel_str():

    zettel = Zettel()
    zettel.load("./examples/220612-1235.md")

    assert isinstance(str(zettel), str)


def test_zettel_eq():

    z1 = Zettel()
    z1.load("./examples/220612-1235.md")

    z2 = Zettel()
    z2.load("./examples/220612-1235.md")

    assert z1 == z2
