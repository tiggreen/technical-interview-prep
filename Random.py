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
	
def main():
	n = int(input("n: "))
	print(decToBinary(n))

main()