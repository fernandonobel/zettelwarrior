from zettelwarrior import zettelwarrior


def test_read_yaml_front_matter():

    result = zettelwarrior.read_yaml_front_matter("./examples/example_note.md")

    expected = {
        "title": "This is the title of the example note.",
        "id": "220612-1235",
        "tags": ["example-note", "test"],
        "status": None,
        "backlink": None,
    }

    assert result == expected
