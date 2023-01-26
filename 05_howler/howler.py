#!/usr/bin/env python3
"""
Author : Jeffrey Schmid-Paz
Date   : 2023-01-25
Purpose: Howler (upper-cases input)
"""

import argparse
import os


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

    if os.path.isfile(args.input):
        in_fh = open(args.input)
        input_text = in_fh.read()
        in_fh.close()
    else:
        input_text = args.input

    if args.outfile != "":
        out_fh = open(args.outfile, "wt")
        out_fh.write(input_text.upper())
        out_fh.close()
    else:
        print(input_text.upper())


# --------------------------------------------------
if __name__ == "__main__":
    main()
