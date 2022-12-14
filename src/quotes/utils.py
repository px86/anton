"""Utility functions for getting quotes."""
from os.path import join, dirname
from random import randint
from typing import List


quotes = []


def read_quotes_from_file(filepath: str) -> List[str]:
    """Read quotes from given file.

    Quotes should be one per line.
    """
    with open(filepath) as f:
        quotes = [q.strip() for q in f if len(q) > 0]
    return quotes


def write_quotes_to_file(quotes: List[str], filepath: str):
    """Write quotes to given file."""
    with open(filepath, "w") as f:
        f.writelines(quotes)


def __initialize():
    """Initialize the quotes global variable."""
    global quotes, quotes_file
    quotes_file = join(dirname(__file__), "resources", "quotes.txt")
    quotes = read_quotes_from_file(quotes_file)


__initialize()


def get_quote() -> str:
    """Get a quote from the collection."""
    i = randint(0, len(quotes))
    return quotes[i]


def add_quote(quote: str):
    """Add a quote to the collection."""
    global quotes
    if len(quote) > 0:
        quotes.append(quote)
        write_quotes_to_file(quotes, quotes_file)
