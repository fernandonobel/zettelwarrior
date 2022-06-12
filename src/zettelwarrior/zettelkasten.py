import glob

from tabulate import tabulate
from zettelwarrior.zettel import Zettel


class Zettelkasten:
    """Class for handling the main directory of Zettelkasten."""

    def __init__(self):
        """Init the Zettelkasten."""

        self.path = "/home/nobel/Sync/Vault/zettelkasten/"
        self.zettels = []

        for filepath in glob.glob(self.path + "*-*.md"):
            zettel = Zettel()
            zettel.load(filepath)

            self.zettels.append(zettel)

        for zettel in self.zettels:
            print(zettel.title)

    def list_all_zettels(self):

        table = []

        for zettel in self.zettels:
            row = []
            row.append(zettel.title)
            row.append(zettel.tags)
            row.append(zettel.uuid)

            table.append(row)

        headers = [
            "Title",
            "Tags",
            "UUID",
        ]

        print()
        print(tabulate(table, headers))
        print()
