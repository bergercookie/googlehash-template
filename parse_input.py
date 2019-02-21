from basic_types import Problem


def parse_input(f_in: str):
    """Parse the input file, fill and return the `Problem` class instance."""

    # Read all contents - line by line
    with open(f_in, 'r') as f:
        conts = [[int(s) for s in i.rstrip().split()] for i in f.readlines()]

    # Remove last line if empty
    if conts[-1] == '':
        conts = conts[:-1]

    # Total values

    # Get rest of items

    # Print stuff out
    print("=" * 80)
    print()
    print("=" * 80)

    return Problem()

