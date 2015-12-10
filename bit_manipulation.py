# Bit Manipulation problems

# x << y
# Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros).
#  This is the same as multiplying x by 2**y.
#
# x >> y
# Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y.
#
# x & y
# Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.
#
# x | y
# Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.
#
# ~ x
# Returns the complement of x - the number you get by switching each 1 for a 0 and each 0
# for a 1. This is the same as -x - 1.
#
# x ^ y
# Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit
# in x if that bit in y is 0, and it's the complement of the bit in x if that bit in y is 1.
#
# Source: https://wiki.python.org/moin/BitwiseOperators

def get_bit(num, i):
	"""return the i-th bit of num"""
	return (num & (1 << i) != 0)

def set_bit(num, i):
	"""set the i-th bit of num."""
	return (num | (1 << i))


# You are given two 32-bit numbers, N and M, and two bit positions, 
# i and j. Write a method to set all bits between i and j in N equal 
# to M (e.g., M becomes a substring of N located at i and starting at j).
# EXAMPLE:
# Input: N = 10000000000, M = 10101, i = 2, j = 6
# Output: N = 10001010100
def update_bits(n, m, i, j):
	mx = ~0 # all 1's
	#1's through position j then 0's
	left = mx - ((1 << j) - 1)
	#1's after position i
	right = ((1 << i) -1)
	#1's, with 0's between i and j.
	mask = left | right
	# clear i through j then put m in there
	return (n & mask) | (m << i)

def is_power_of_2(n):
	"""
	Check if given n is power of 2 or not. Like 2, 8, 16, 256
	"""
	# ~ is the compliment of n
	return (n & ~n) == 0

def main():
	print(is_power_of_2(16) == True)
	print(is_power_of_2(256) == True)
	print(is_power_of_2(2) == True)
	print(is_power_of_2(7) == False)
	print(is_power_of_2(156) == False)


if __name__ == '__main__':
	main()