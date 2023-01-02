#!/usr/bin/env python
"""
Author : Jeffrey Schmid-Paz
Date   : 2023-01-02
Purpose: Warn captain for a something near the ship
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("word", metavar="word", help="A word")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Run the program"""

    args = get_args()
    word = args.word

    print(word)


# --------------------------------------------------
if __name__ == "__main__":
    main()
