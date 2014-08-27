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
	
	
def main():
	if len(sys.argv) != 3:
		raw_input("Usage: python Anagram.py str1 str2")
		return 
		
	print isAnagramSorted(sys.argv[1], sys.argv[2])
	
main()