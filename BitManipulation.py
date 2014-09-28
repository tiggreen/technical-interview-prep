
# Return the i-th bit of num.
def getBit(num, i):
	return (num & (1 << i) != 0)

# Set's the i-th bit of num.
def setBit(num, i):
	return (num | (1 << i))
	
def main():
	# 111
	if(getBit(8,2)):
		print(1)
	else:
		print(0)
		
	setBit(8,3)

main()