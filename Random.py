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
		
	
def main():
	# n = int(input("n: "))
	a = [1,2,3,11,18,25]
	b = [4,5,6,7,12,19,24]
	str = "My name is Tigran"
	print(binarySearchRec(a, 11))
	# print(reverseWordsInPlace(str))


main()