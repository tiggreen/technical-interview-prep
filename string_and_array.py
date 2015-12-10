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


# insert, remove or replace only one char
# you can get from st1 -> st2
def one_edit_char(st1, st2):
    if abs(len(st1) - len(st2)) > 1:
        return False

    if _one_edit_replace(st1, st2):
        return True

    if _one_edit_remove(st1, st2):
        return True

    if _one_edit_remove(st2, st1):
        return True

    return False

def _one_edit_replace(st1, st2):
    """
    Check if st1 and st2 are one char replace away from each other.
    """
    if len(st1) != len(st2):
        return False

    is_diff_char_found = False

    for i in range(len(st1)):
        if st1[i] != st2[i]:
            # we already found one char difference so return False
            if is_diff_char_found:
                return False
            else:
                is_diff_char_found = True

    return True


def _one_edit_remove(st1, st2):
    """
    Check to see if we can get st2 from st1 by removing one char element
    """
    for i in range(len(st1)):
        if st1[:i] + st1[i+1:] == st2:
            return True
    return False


def compress(st):
    current = 0
    compressed_string = ""

    while current < len(st):
        runner = current + 1
        cnt  = 1
        while runner < len(st) and st[runner] == st[current]:
            cnt = cnt + 1
            runner = runner + 1
        compressed_string = compressed_string + (st[current] + str(cnt))
        # move current forward to the runner's position
        current = runner

    if len(st) < len(compressed_string):
        return st

    return compressed_string

# find a pair that sum to a given S. find a (x,y) pair that x + y = s, or x = s - y
# s = 8, [1, 3, 4, 7]
# d = {1, 3, 4,  } (el, sum - el)
def find_sum_pair(arr, s):
    # if arr is None just return
    # create a new hashtable
    # go over each el in arr
    #   1. check if s - el is in D values, then return (el, d[el])
    #   1. if not there then add el to the dict
    if arr is None:
        return None

    d = {}
    for el in arr:
        sub = s - el
        if sub in d:
            return (el, sub)
        else:
            d[el] = sub
    return None

# if not in place we can always use stack to do this, push and pop and you got it!
def reverse_words_in_place(sentence):
    # my name is Tigran => Tigran is name my
    sentence_array = sentence.split()
    # base case
    if len(sentence_array) == 1:
        return sentence_array[0]
    last = sentence_array[-1]
    first = " ".join(sentence_array[:-1])

    return last + " " + reverse_words_in_place(first)

def main():
    str1 = sys.stdin.read()
    str2 = sys.stdin.read()
    if isAnagramArr(str1, str2):
        sys.stdout.write("Anagrams!")
    else:
        sys.stdout.write("Not anagrams!")

if __name__ == "__main__":
    main()
