import datetime
import glob
import os

from tabulate import tabulate
from zettelwarrior.zettel import Zettel


class Zettelkasten:
    """Class for handling the main directory of Zettelkasten."""

    def __init__(self, path):
        """Init the Zettelkasten."""

        self.path = path
        self.zettels = []

        for filepath in glob.glob(self.path + "*-*.md"):
            zettel = Zettel()
            zettel.load(filepath)

            self.zettels.append(zettel)

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

    def print_tags(self):

        tags = {}

        for zettel in self.zettels:
            for tag in zettel.tags:
                if tag not in tags:
                    tags[tag] = []
                tags[tag].append(None)

        table = []

        for tag in tags:
            row = []
            row.append(tag)
            row.append(len(tags[tag]))

            table.append(row)

        headers = ["Tag", "Count"]

        print()
        print(tabulate(table, headers))
        print()

    def add_zettel(self, title=None):
        """Add a new zettel to the zettelkasten."""

        e = datetime.datetime.now()

        uuid = ""
        uuid += f"{str(e.year)[-2:]}"
        uuid += f"{e.month:02d}"
        uuid += f"{e.day:02d}"
        uuid += "-"
        uuid += f"{e.hour:02d}"
        uuid += f"{e.minute:02d}"

        filepath = self.path + uuid + ".md"

        f = open(filepath, "x")

        f.write("---\n")
        f.write(f'title: "{title}"\n')
        f.write(f"uuid: {uuid}\n")
        f.write("tags: []\n")
        f.write("status:\n")
        f.write("backlink:\n")
        f.write("---\n")
        f.write("\n")
        f.write("----\n")
        f.close()

        os.system(f"vim {filepath}")

        print(f"Created Zettel with UUID: {uuid}")
