# @tiggreen

# This problem is also called Min Cost Path problem.
def getFastestPath(grid):
	
	m = len(grid)
	n = len(grid[0])
	
	totalTime = [[ 0 for i in range(n)] for j in range(m)]
	totalTime[0][0] = grid[0][0]
	
	# initialize the first column
	for i in range(1,m):
		totalTime[i][0] = totalTime[i-1][0] + grid[i][0]
	
	# initialize the first row
	for j in range(1,n):
		totalTime[0][j] = totalTime[0][j-1] + grid[0][j]
		
	for i in range(1,m):
		for j in range(1,n):
			totalTime[i][j] = min(totalTime[i][j-1], totalTime[i-1][j]) + grid[i][j]
	
	return totalTime[m-1][n-1]

	
def main():
	grid = [[3,2,1,4],[3,1,2,1],[4,5,6,7], [1,2,1,1]]
	print(grid)
	print(getFastestPath(grid))

main()