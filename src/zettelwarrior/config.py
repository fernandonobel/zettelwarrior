import configparser
from dataclasses import dataclass
import os
from pathlib import Path


@dataclass
class Config:
    """Class for handling the configuration options of
    ZettelWarrior."""

    path: Path = None

    def user_home_path(self):
        return Path(os.path.expanduser("~"))

    def load_user_config(self):
        config_path = self.user_home_path() / ".zwrc"
        self.load_config_file(config_path)

    def load_config_file(self, config_path):
        config_file = configparser.ConfigParser()
        config_file.read(config_path)
        self.path = Path(config_file["zettelwarrior"]["path"])
