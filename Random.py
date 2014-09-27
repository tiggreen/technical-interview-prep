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
		n = int(n/2)
		
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
		
	midInd = (int)(len(lst)/2)
	
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
			print(counter)
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
				
	return perms
	
		
def main():
	# n = int(input("n: "))
	a = [1,2,3,11,18,25]
	b = [4,5,6,7,12,19,24]
	str = "My name is Tigran"
	#res = getAllPermutations("ABC")
	ls = ["a","b"]
	#print(getPowerSet(ls))
	#lst = [1,3,4,6,12,16,19, 10,9]
	# should return (12, 16)
	#print(findPairSum(lst, 10))
	st = "My name is Tigran"
	#print(reverseWordsInPlace(str))
	s = "abc"

	print(getAllPerms(s))
	


main()