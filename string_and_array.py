# author: @tiggreen
import sys

def reverse_string(str):
    """"
    [begin:end:step] - by leaving begin and end off
    and specifying a step of -1, it reverses a string.
    """
    return str[::-1]

def is_anagram_sorted(str1, str2):
    """
    This methods checks if two given strings are anagrams or not.
    An anagram of a string is another string that contains same characters,
    only the order of characters can be different.

    1. One aproach will be to sort both strings and check if they're equal.
    2. The other approach can be to use an array of booleans. 
    """
    return sorted(str1) == sorted(str2)

def is_anagram_arr(str1, str2):
    if len(str1) != len(str2):
        return False

    arr = [False for i in range(1024)] # or 256 for ASCII strings
    for i in str1:
        v = ord(i)
        arr[v] = True
    for j in str2:
        b = ord(j)
        if arr[b] != True:
            return False

    return True


def main():
    str1 = sys.stdin.read()
    str2 = sys.stdin.read()
    if isAnagramArr(str1, str2):
        sys.stdout.write("Anagrams!")
    else:
        sys.stdout.write("Not anagrams!")

if __name__ == "__main__":
    main()
