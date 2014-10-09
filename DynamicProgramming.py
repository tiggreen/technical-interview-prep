# @tiggreen

# This problem is also called Min Cost Path problem.
# Returns the total min cost as well as the path.
def getFastestPath(grid):
	
	m = len(grid)
	n = len(grid[0])
	path = [[ 0 for i in range(n)] for j in range(m)]

	totalTime = [[ 0 for i in range(n)] for j in range(m)]
	totalTime[0][0] = grid[0][0]
	
	# initialize the first column
	for i in range(1,m):
		path[i][0] = 2
		totalTime[i][0] = totalTime[i-1][0] + grid[i][0]
	
	# initialize the first row
	for j in range(1,n):
		path[0][j] = 1
		totalTime[0][j] = totalTime[0][j-1] + grid[0][j]
	
		
	for i in range(1,m):
		for j in range(1,n):
			tempMin = min(totalTime[i][j-1], totalTime[i-1][j])
			if tempMin == totalTime[i][j-1]:
				path[i][j] = 1
			else:
				# from top 
				path[i][j] = 2
			totalTime[i][j] = tempMin + grid[i][j]
			
	cir = m - 1
	cic = n -1
	
	print((cir, cic))
	
	while cir != 0 or cic != 0:
		if path[cir][cic] == 1:
			print((cir, cic - 1))
			cic -= 1
		else:
			print((cir -1, cic))
			cir -= 1
	
	
	return (path, totalTime[m-1][n-1])

def printGrid(grid):
	for i in range(len(grid)):
		print(grid[i])	
	
	print()

#Returns the i-th fibonacci number. DP.
buf = [0 for i in range(10000)]
def fib(i):
	if i == 0:
		return 0
	if i == 1:
		return 1
	if buf[i] != 0:
		return buf[i]
	buf[i] = fib(i-1) + fib(i-2)
	return buf[i]	
	
	
	
"""
Longest Increasing Subsequence.

{10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 
and LIS is {10, 22, 33, 50, 60, 80}.
"""
def LIS(arr):
	
	lis = [1 for i in range(len(arr))]
	elems = []
	
	for i in range(1, len(arr)):
		for j in range(i):
			if arr[i] > arr[j] and lis[i] < lis[j] + 1:
				lis[i] = lis[j] + 1
	
	mx = 0
	for el in lis:
		if el > mx:
			mx = el
			
			
	for i in range(len(lis)-1):
		if lis[i+1] > lis[i]:
			elems.append(arr[i+1])
			
	return (mx, elems)
	
def main():
	print(LIS([99, 22, 9, 33, 21, 50, 41, 60, 80]))

main()