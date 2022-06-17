import datetime
from pathlib import Path

from tabulate import tabulate
from zettelwarrior.zettel import Zettel


class Zettelkasten:
    """Class for handling the main directory of Zettelkasten."""

    def __init__(self, path):
        """Init the Zettelkasten."""

        self.path = Path(path)
        self.zettels = []

        for filepath in self.path.glob("*-*.md"):
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

    def tags(self):

        result = {}

        for zettel in self.zettels:
            for tag in zettel.tags:
                if tag not in result:
                    result[tag] = []
                result[tag].append(zettel)

        return result
    

    def generate_tags_index(self):

        file = open(self.path / "tags.md", "w")

        file.write("# Tags\n")
        file.write("\n")

        tags = self.tags()

        for tag in tags:
            file.write(f"## {tag}\n")
            file.write("\n")

            for zettel in tags[tag]:
                file.write(f"* [{zettel.title}]({zettel.uuid})\n")
            
            file.write("\n")

        file.close()


    def print_tags(self):

        tags = self.tags()
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

    def get_now(self):
        return datetime.datetime.now()

    def generate_new_uuid(self, now=None):

        if now is None:
            now = self.get_now()

        result = ""
        result += f"{str(now.year)[-2:]}"
        result += f"{now.month:02d}"
        result += f"{now.day:02d}"
        result += "-"
        result += f"{now.hour:02d}"
        result += f"{now.minute:02d}"

        return result

    def add_zettel(self, title=None):
        """Add a new zettel to the zettelkasten."""

        uuid = self.generate_new_uuid()

        filename = uuid + ".md"

        filepath = self.path / filename

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

        return filepath, uuid
