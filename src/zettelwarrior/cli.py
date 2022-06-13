import click
from zettelwarrior.zettel import Zettel
from zettelwarrior.zettelkasten import Zettelkasten


@click.group()
def cli():
    """ZettelWarrior Command Line Interface."""


@cli.command(short_help="Shows data and metadata of a Zettel")
@click.argument("filename", type=click.Path(exists=True))
def information(filename):

    zettel = Zettel()
    zettel.load(filename)

    print()
    print(zettel)
    print()


@cli.command(short_help="Show list of all Zettels")
def list():

    zettelkasten = Zettelkasten()
    zettelkasten.list_all_zettels()


@cli.command(short_help="Show list of all tags used")
def tags():

    zettelkasten = Zettelkasten()
    zettelkasten.print_tags()


@cli.command(short_help="Add a new Zettel")
def add():

    zettelkasten = Zettelkasten()
    zettelkasten.add_zettel()


def main():
    cli(obj={})


if __name__ == "__main__":
    main()
