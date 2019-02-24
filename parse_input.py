from basic_types import Problem
from utils import print_, print_sec, print_ssec, sep, ssep


def parse_input(f_in: str):
    """Parse the input file, fill and return the `Problem` class instance."""
    print_ssec("parsing input...")

    # Read all contents - line by line
    # TODO - Change me if not dealing with ints!!!
    with open(f_in, 'r') as f:
        conts = [[int(s) for s in i.rstrip().split()] for i in f.readlines()]

    # Remove last line if empty
    if conts[-1] == '':
        conts = conts[:-1]

    # Total values

    # Get rest of items

    # Print stuff out
    print_ssec("Inputs: ")

    print_("parsed input successfully")
    return Problem()

