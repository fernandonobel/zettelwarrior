from zettelwarrior.zettel import Zettel
from zettelwarrior.zettelkasten import Zettelkasten

def test_zettelkasten():

    zettelkasten = Zettelkasten("./examples/")

    expected = [
        Zettel().load("./examples/220612-1235.md")
    ]

    assert zettelkasten.zettels == expected
