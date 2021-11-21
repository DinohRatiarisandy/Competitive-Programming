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
	rows = len(grid)
	
	if rows==0:
		return -1

	cols  		  = len(grid[0])
	fresh_oranges = 0
	rotten		  = deque()

	for r in range(rows):
		for c in range(cols):
			if grid[r][c]==2:
				rotten.append((r, c))
			elif grid[r][c]==1:
				fresh_oranges += 1

	minutes_elapsed = 0

	while rotten and fresh_oranges:
		minutes_elapsed += 1
		for _ in range(len(rotten)):
			x, y = rotten.popleft()
			for dx, dy in [(1, 0,), (-1, 0,), (0, 1,), (0, -1,),]:
				xx = x+dx
				yy = y+dy
				if xx<0 or xx==rows or yy<0 or yy==cols:
					continue
				if grid[xx][yy]==2 or grid[xx][yy]==0:
					continue
				fresh_oranges  -= 1
				grid[xx][yy] 	= 2
				rotten.append((xx, yy,))

	return minutes_elapsed if fresh_oranges==0 else -1

if __name__ == "__main__":

	grid = [[2,1,1],[1,1,0],[0,1,1]]
	print(solve(grid))