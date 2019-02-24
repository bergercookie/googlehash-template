from basic_types import Problem
from utils import print_, print_sec, print_ssec


def export_results(p: Problem, f_out: str):
    """Export the results to the file specified."""

    print_ssec("Exporting results to {}".format(f_out))
    print_("Exported.")
