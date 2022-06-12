import os
import click

from zettelwarrior.zettelwarrior import read_yaml_front_matter
from zettelwarrior.zettel import Zettel


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
    

def main():
    cli(obj={})


if __name__ == "__main__":
    main()
