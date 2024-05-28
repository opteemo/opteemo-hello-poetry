import argparse

from . import hello, __version__


def cli():
    parser = argparse.ArgumentParser(prog='Hello', description='A command to say hello !')
    parser.add_argument('-v', '--version', action='version', version=__version__)
    parser.parse_args()

    hello()


if __name__ == "__main__":
    cli()
