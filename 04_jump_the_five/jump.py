#!/usr/bin/env python3
"""
Author : Jeffrey Paz-Schmid
Date   : 2023-01-22
Purpose: Encode Phone-Numbers
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Jump the Five",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("positional", metavar="str", help="Input text")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    pos_arg = args.positional

    jumper = {
        "1": "9",
        "2": "8",
        "3": "7",
        "4": "6",
        "5": "0",
        "6": "4",
        "7": "3",
        "8": "2",
        "9": "1",
        "0": "5",
    }

    for char in pos_arg:
        if char in jumper:
            print(jumper[char], end="")
        else:
            print(char, end="")


# --------------------------------------------------
if __name__ == "__main__":
    main()
