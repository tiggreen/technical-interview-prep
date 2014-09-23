# author: @tiggreen
import sys

"""
This methods checks if two given strings are anagrams or not.
An anagram of a string is another string that contains same characters, 
only the orderof characters can be different.

1. One aproach will be to sort both strings and check if they're equal. 
2. The other approach can be to use an array of booleans. 
"""


def isAnagramSorted(str1, str2):
    return sorted(str1) == sorted(str2)

def isAnagramArr(str1, str2):
	if len(str1) != len(str2):
		return False
	arr = [False for i in range(1024)]
	for i in str1:
		v = ord(i)
		arr[v] = True
    
	for j in str2:
		b = ord(j)
		if arr[b] != True:
			return False
	return True


def main():
    # if len(sys.argv) != 3:
    #     input("Usage: python Anagram.py str1 str2")
    #     return
    #
    str1 = sys.stdin.read()
    str2 = sys.stdin.read()
    if isAnagramArr(str1, str2):
        sys.stdout.write("Anagrams!")
    else:
        sys.stdout.write("Not anagrams!")
	

    #print(isAnagramArr(sys.argv[1], sys.argv[2]))


main()
