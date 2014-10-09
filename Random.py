# @tiggreen
# Some random type of problems. 

"""
	Converts the decimal (10 based) number to a binary number
	decToBinary(8) => 1000
"""
def decToBinary(n):
	ret = list()
	while (n > 1):

		if n % 2 == 0:
			ret.insert(0,0)
		else:
			ret.insert(0,1)
		n = n//2
		
	ret.insert(0,1)
	return ret

# My name is Tigran" --> "Tigran is name my"
# Will be imlemented in place and recursive
def reverseWordsInPlace(str):
	if len(str.split()) == 1:
		return str
	return str.split()[-1] + " " + reverseWordsInPlace(' '.join(str.split()[:-1]))

"""
[1, 2, 3], [4, 5, 6, 7] ==> [1, 2, 3, 4, 5, 6, 7]

"""
def mergeSortedLists(lst1,lst2):
	#let's check if one of them is empty
	if (len(lst1) == 0):
		 return lst2
	if (len(lst2) == 0):
		 return lst1
	
	i = 0
	j = 0
	# idealy we want to have len(lst1) + len(lst2) size list
	resultList = []
	while (i < len(lst1) and j < len(lst2)):
		if (lst1[i] < lst2[j]):
			resultList.append(lst1[i])
			i+=1
		else:
			resultList.append(lst2[j])
			j+=1
			
	while i < len(lst1):
		resultList.append(lst1[i])
		i+=1
	while j < len(lst2):
		resultList.append(lst2[j])
		j+=1
		
	return resultList
	# there might be some leftover elements in lists so let's
	# check it out. 
	
# let's try to find the data in the given list.	 
# Returns true if we can find the data.
def binarySearchRec(lst, data):
	if lst == []:
		return False
		
	midInd = len(lst)//2
	
	if lst[midInd] == data:
		return True
	if data < lst[midInd]:
		return binarySearchRec(lst[:midInd], data)
	elif data > lst[midInd]:
		return binarySearchRec(lst[midInd+1:], data)

"""
Returns all the permutations of the string.
E.g. "abc" => "abc", "acb", "bac", "bca", "cab", "cba" 
"""

def getAllPermutations(st):
	perms = []
	if st == None:
		return st
	# the base case. 
	if len(st) == 0:
		perms.append('')
		return perms
	else:
		first = st[0]
		remainder = st[1:]

		words = getAllPermutations(remainder)
		for w in words:
			for i in range(len(w)+1):
				perms.append(insertCharAt(w, first,i))
		return perms

def insertCharAt(st, f, pos):
	result = st[:pos] + f + st[pos:]
	return result

# ls = [a,b] => [[], a, b, [a,b]]
def getPowerSet(ls):
	allSubsets = []
	sz = 1 << len(ls)
	for counter in range(sz):
		tempSubset  = []
		for j in range(len(ls)):
			if (counter & 1 << j) > 0:
				tempSubset.append(ls[j])
		allSubsets.append(tempSubset)
	return allSubsets
	
"""
Finding pair of numbers in a list that add to given sum.
a = [1,3,4,6,12,16,19, 10]
findPairSum(a, 28) => (12,16)
key : sum - x, value y
"""
def findPairSum(lst, sm):
	if not lst:
		return lst
	d = dict()
	result = []
	for i in lst:
		if i not in d:
			d[sm - i] = i
		else:
			key = sm - i
			result.append((key,i))
			
	return result

def getAllPerms(st):
	perms = []
	
	if st == '':
		perms.append('')
		return perms 
	
	firstChars = st[:-1]
	lastChar = st[-1]
	allPerms = getAllPerms(firstChars)
	
	for s in allPerms:
		for i in range(len(s) + 1):
			temp = insertCharAt(s, lastChar, i)
			perms.append(temp)
	print(perms)			
	return perms

# Print all valid combinations of n-pairs of parentheses.
def printAllParens(cnt):
	st = ['' for i in range(cnt*2)]
	return printAllParensUtil(cnt, cnt, 0, st)
	
def printAllParensUtil(left, right, cnt, st):
	
	if left < 0 or left > right:
		return 
	if left == 0 and right == 0:
		print(st)
	else:
		if left > 0:
			st[cnt] = '('
			printAllParensUtil(left-1, right, cnt+1, st)
			
		if right > left:
			st[cnt] = ')'
			printAllParensUtil(left, right-1, cnt+1, st)

#Calculate x raised to the power n */
def pow(x,n):
	if n == 0:
		return 1
	elif n % 2 == 0:
		return pow(x, n//2)*pow(x, n//2)
	else:
		return x*pow(x, n//2)*pow(x, n//2)
		
"""
Given an input string and a dictionary of words, find out if
the input string can be segmented into a space-separated sequence of 
dictionary words. See following examples for more details.
"""
def wordBreak(st, dic):
	#base case
	if len(st) == 0:
		return True
	for i in range(1,len(st) + 1):
		if st[0:i] in dic and wordBreak(st[i:len(st)-i], dic):
			return True
	return False

"""
"abcdbfa" => "cdbfa" (do this in place)
Q: Do we want to remove first occurance chars or the second, or next?
"""
def removeDuplicates(st):
	if st == None:
		return None
	# let this be the base case
	if st == "":
		return st
		
	head = st[0]
	tail = st[1:]
	
	if head in tail:
		return removeDuplicates(tail)
	else:
		return head + removeDuplicates(tail)
		
def reverseString(st):
	if st is None:
		return None
	if st == "":
		return st
	return st[-1] + reverseString(st[:-1])

# Reverse the digits of the integer
# 12345 -> 54321

def reverseDigits(num):
	newnum  = 0
	while num > 0:
		digit = num % 10
		num = num // 10
		newnum = newnum*10 + digit
	
	return newnum		
	
def main():
	print(reverseDigits(1))
	
if __name__ == '__main__':
	main()