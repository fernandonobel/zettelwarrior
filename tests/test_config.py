from pathlib import Path
from zettelwarrior.config import Config

def test_config():

    config = Config()

    assert isinstance(config, Config)

def test_load_user_config():

    result = Config()
    result.load_user_config()

    expected = Config()
    expected.path = Path("/home/nobel/Sync/zettelkasten")

    assert result == expected

def test_load_config_file(tmpdir):

    result = Config()
    result.load_config_file("./examples/.zwrc")

    expected = Config()
    expected.path = Path("./examples")

    assert result == expected
