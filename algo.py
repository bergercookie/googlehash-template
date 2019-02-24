#!/usr/bin/env python3

from export_results import export_results
import os
from parse_input import parse_input
import sys
import basic_types
import time
from utils import print_, print_sec, print_ssec

# Main body of the hashcode algorithm

def main():
    if len(sys.argv) != 2:
        print("Usage: {} <path-to-input-file>".format(sys.argv[0]))
        exit(1)

    # Parse inputs
    input_f = sys.argv[1]
    # name of the current case
    fname = os.path.basename(input_f)
    print_sec("Running for case: {}".format(fname))

    if not os.path.isfile(input_f):
        raise FileNotFoundError(input_f)

    # Parse input - use serial form if it's there
    prob = parse_input(input_f)

    # Process
    print_ssec("computing...")
    # TODO
    print_("compuations done.")

    # Export results
    outfile = "{}_{}".format(int(time.time()), fname)
    export_results(prob, outfile)

    print_("all done, exiting.")


if __name__ == "__main__":
    main()
