"""
Checks if the give string contains unique characters.

Author @tiggreen
"""
import sys

def isUnique(str):
	lst = list()
	"""
	Good thing to notice here is that lst is an empty list and 
	if you're attempting to write to element [0] (lst[0] = False) in the 
	first iteration it will trow an exception since lst[0] doesn't exist yet.
	"""

	for j in range(1024):
		lst.append(False)
		 
	for i in str:
		ind = ord(i)
		if (lst[ind] == True):
			return False
		else:
			lst[ind] = True
	return True
		
	
def main():
	print "{0} is the answer for string {1}".format(isUnique(sys.argv[1]), sys.argv[1])

main()	