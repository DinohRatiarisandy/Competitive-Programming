from sys import stdin

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())


def nums_islands(grid):
	height   = len(grid)
	width    = len(grid[0])
	visited  = set()
	islands  = 0
	for row in range(len(grid)):
		for col in range(len(grid[row])):
			if int(grid[row][col]) and (row, col) not in visited:
				to_visit = [(row, col)]
				visited.add((row, col))
				# print(to_visit)
				while to_visit:
					ii, jj = to_visit.pop()
					for i, j in [(ii, jj-1), (ii+1, jj), (ii, jj+1), (ii-1, jj)]:
						if 0<=i<height and 0<=j<width and (i, j) not in visited\
						and int(grid[i][j]):
							visited.add((i, j))
							to_visit.append((i, j))
				islands += 1

	return islands

if __name__ == "__main__":

	grid = [
	  ["1","1","0","1","0"],
	  ["1","1","0","0","1"],
	  ["0","0","1","0","0"],
	  ["1","0","0","1","1"]
	]
	
	grid2 = [
	  ["1","1","0","0","0"],
	  ["1","1","0","0","0"],
	  ["0","0","1","0","0"],
	  ["0","0","0","1","1"]
	]

	print(nums_islands(grid))