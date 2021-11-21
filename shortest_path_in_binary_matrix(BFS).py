from sys import stdin
from collections import deque

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())


def solve(grid):
	height = len(grid)
	widht  = len(grid[0])

	if grid[0][0]!=0 or grid[height-1][widht-1]!=0:
		return -1

	if height==1 and grid[0][0]==0:
		return 1

	visited  = set((0, 0))
	to_visit = deque([(0, 0)])
	length_of_clear_path = 1

	while to_visit:
		# print(to_visit)
		for _ in range(len(to_visit)):
			ii, jj = to_visit.popleft()
			for i, j in [(ii, jj-1), (ii, jj+1), (ii+1, jj), (ii-1, jj),\
						(ii-1, jj-1), (ii-1, jj+1), (ii+1, jj-1), (ii+1, jj+1)]:
				if 0<=i<height and 0<=j<widht and (i, j) not in visited \
						and grid[i][j]==0:
					visited.add((i, j))
					to_visit.append((i, j))
					if i==height-1 and j==widht-1:
						return length_of_clear_path+1
		length_of_clear_path += 1
	return -1

if __name__=="__main__":

	grid1 = [
		[0, 0, 0],
		[1, 1, 0],
		[1, 1, 0]
	]
	grid = [
		[0, 0, 1],
		[0, 1, 0],
		[1, 0, 1],
		[0, 1, 1],
		[1, 0, 0]
	]
	grid3 = [
		[0, 1],
		[1, 0]
	]
	print(solve(grid))