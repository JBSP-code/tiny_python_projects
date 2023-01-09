#!/usr/bin/env python3
"""
Author : Jeffrey Schmid-Paz
Date   : 2023-01-05
Purpose: Create a list of items to bring along a picnic
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Picnic game",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("positional", metavar="str", help="Item(s) to bring")

    parser.add_argument("-s", "--sorted", help="Sort the items", action="store_true")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    sort_flag = args.on
    items = args.str

    print(f'flag_arg = "{sort_flag}"')
    print(f'positional = "{items}"')


# --------------------------------------------------
if __name__ == "__main__":
    main()
