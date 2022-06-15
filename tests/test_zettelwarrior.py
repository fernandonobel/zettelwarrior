from zettelwarrior.zettel import Zettel
from zettelwarrior.zettelkasten import Zettelkasten

def test_zettelkasten():

    zettelkasten = Zettelkasten("./examples/")

    assert isinstance(zettelkasten, Zettelkasten)


def test_list_all_zettels():

    zettelkasten = Zettelkasten("./examples/")

    expected = [
        Zettel().load("./examples/220612-1235.md")
    ]

    #assert zettelkasten.zettels == expected

