from zettelwarrior.zettel import Zettel

def test_zettel():

    zettel = Zettel()

def test_load_zettel():
    
    zettel = Zettel()
    zettel.load("./examples/example_note.md")

    assert zettel.title == "This is the title of the example note."
    assert zettel.uuid == "220612-1235"
    assert zettel.tags == ["example-note", "test"]
    assert zettel.status == "done"
    assert zettel.backlink == "<[La metodología Zettelkasten](220610-1709)>"

def test__zettel_str():

    zettel = Zettel()
    zettel.load("./examples/example_note.md")
    str(zettel)
