import os

import click
import pkg_resources
from zettelwarrior.zettel import Zettel
from zettelwarrior.zettelkasten import Zettelkasten

path = "/home/nobel/Sync/zettelkasten/"


@click.group()
@click.version_option(pkg_resources.get_distribution("zettelwarrior").version)
@click.pass_context
def cli(ctx):
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

    zettelkasten = Zettelkasten(path)
    zettelkasten.list_all_zettels()


@cli.command(short_help="Show list of all tags used")
def tags():

    zettelkasten = Zettelkasten(path)
    zettelkasten.print_tags()


@cli.command(short_help="Add a new Zettel")
def add():

    zettelkasten = Zettelkasten(path)
    filepath, uuid = zettelkasten.add_zettel()

    os.system(f"vim {filepath}")
    print(f"Created Zettel with UUID: {uuid}")


@cli.command(short_help="Generate tag index file")
def generate_tag_index():

    zettelkasten = Zettelkasten(path)
    zettelkasten.generate_tag_index()

    print("Generated tag index file: ./tags.md")


def main():
    cli(obj={})


if __name__ == "__main__":
    main()
