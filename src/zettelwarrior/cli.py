import os
import click

from zettelwarrior.zettel import Zettel
from zettelwarrior.zettelkasten import Zettelkasten


@click.group()
def cli():
    """ZettelWarrior Command Line Interface."""


@cli.command(short_help="Shows data and metadata of a Zettel")
@click.argument("filename", type=click.Path(exists=True))
def information(filename):
    """Shows data and metadata of a Zettel."""

    project_dir = os.path.realpath(".")
    filepath = os.path.join(project_dir, filename)

    zettel = Zettel()
    zettel.load(filename)

    print()
    print(zettel)
    print()

@cli.command(short_help="List Zettels")
def list():
    """List Zettels"""

    zettelkasten = Zettelkasten()
    zettelkasten.list_all_zettels()


def main():
    cli(obj={})


if __name__ == "__main__":
    main()