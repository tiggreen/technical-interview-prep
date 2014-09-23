"""
author @tiggreen 
String reversal.

In Python, strings are immutable, so you can't change 
their characters in-place.
"""
import sys


def reverseString(str):
    """"
    [begin:end:step] - by leaving begin and end off
    and specifying a step of -1, it reverses a string.
    """
    return str[::-1]


def main():
    if len(sys.argv) != 2:
        print("Usage: ReverseString.py yourstring")
        return

    str = sys.argv[1]
    print(reverseString(str))


main()
