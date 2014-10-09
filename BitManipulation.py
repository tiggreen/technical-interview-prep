
# Return the i-th bit of num.
def getBit(num, i):
	return (num & (1 << i) != 0)

# Sets the i-th bit of num.
def setBit(num, i):
	return (num | (1 << i))

"""
You are given two 32-bit numbers, N and M, and two bit positions, 
i and j. Write a method to set all bits between i and j in N equal 
to M (e.g., M becomes a substring of N located at i and starting at j).
EXAMPLE:
Input: N = 10000000000, M = 10101, i = 2, j = 6
Output: N = 10001010100
"""

def updateBits(n, m, i, j):
	mx = ~0 # all 1's
	
	#1's through position j then 0's
	left = mx - ((1 << j) - 1)
	
	#1's after position i
	right = ((1 << i) -1)
	
	#1's, with 0's between i and j.
	mask = left | right
	
	# clear i through j then put m in there
	
	return (n & mask) | (m << i)
	
		
def main():
	print(bin(updateBits(16, 16, 0,5)))

main()