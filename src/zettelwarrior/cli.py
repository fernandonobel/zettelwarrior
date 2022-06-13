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

    zettel = Zettel()
    zettel.load(filename)

    print()
    print(zettel)
    print()


@cli.command(short_help="Show list of all Zettels")
def list():
    """List Zettels"""

    zettelkasten = Zettelkasten()
    zettelkasten.list_all_zettels()


@cli.command(short_help="Show list of all tags used")
def tags():
    """Show list of all tags used"""

    zettelkasten = Zettelkasten()
    zettelkasten.print_tags()


def main():
    cli(obj={})


if __name__ == "__main__":
    main()
