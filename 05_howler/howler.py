#!/usr/bin/env python3
"""
Author : Jeffrey Schmid-Paz
Date   : 2023-01-25
Purpose: Howler (upper-cases input)
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Howler (upper-cases input)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("input", metavar="text", help="Input string or file")

    parser.add_argument(
        "-o", "--outfile", help="Output filename", metavar="str", type=str, default="",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Process the arguments"""

    args = get_args()
    outfile_arg = args.outfile
    input_arg = args.input

    if outfile_arg != "":
        out_fh = open(outfile_arg, "wt")
        out_fh.write(input_arg.upper())
        out_fh.close()
    else:
        print(input_arg.upper())


# --------------------------------------------------
if __name__ == "__main__":
    main()
