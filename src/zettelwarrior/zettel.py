from tabulate import tabulate
import yaml


class Zettel:
    """Class for handling the data of a Zettel."""

    def __init__(self):
        """Init a Zettel"""

        self.title = None
        self.uuid = None
        self.tags = None
        self.status = None
        self.backlink = None

    def read_front_matter(self, filepath):

        with open(filepath, "r") as f:
            # Make a dict from the first YAML block
            result = next(yaml.load_all(f, Loader=yaml.FullLoader))

        return result

    def load(self, filepath):

        front_matter = self.read_front_matter(filepath)

        self.title = front_matter.get("title", None)
        self.uuid = front_matter.get("uuid", None)
        self.tags = front_matter.get("tags", None)
        self.status = front_matter.get("status", None)
        self.backlink = front_matter.get("backlink", None)

        return self

    def __str__(self):

        table = []

        table.append(["Title", self.title])
        table.append(["UUID", self.uuid])
        table.append(["Tags", self.tags])
        table.append(["Status", self.status])
        table.append(["Backlink", self.backlink])

        result = tabulate(table, headers=["Name", "Value"])

        return result

    def __eq__(self, other):

        if not isinstance(other, Zettel):
            return False

        if not self.title == other.title:
            return False

        if not self.uuid == other.uuid:
            return False

        if not self.tags == other.tags:
            return False

        if not self.backlink == self.backlink:
            return False

        return True
