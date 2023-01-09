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

    parser.add_argument("items", metavar="str", help="Item(s) to bring", nargs="+")

    parser.add_argument("-s", "--sorted", help="Sort the items", action="store_true")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    sort_flag = args.sorted
    items = args.items

    if sort_flag == True:
        items.sort()

    if len(items) >= 3:
        items.insert(-1, "and ")
        items_to_bring = ", ".join(items[:-1]) + items[-1]
    elif len(items) == 2:
        items_to_bring = " and ".join(items)
    else:
        items_to_bring = items[0]

    print("You are bringing " + items_to_bring + ".")


# --------------------------------------------------
if __name__ == "__main__":
    main()
