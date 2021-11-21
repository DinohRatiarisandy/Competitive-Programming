from sys import stdin

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())


def max_area_of_island(grid):
	height = len(grid)
	width  = len(grid[0])
	seen   = set()
	island = 0
	for i in range(height):
		for j in range(width):
			if grid[i][j] and (i, j) not in seen:
				shape = 0
				to_visit = [(i, j)]
				seen.add((i, j))
				while to_visit:
					il, jl = to_visit.pop()
					shape += 1
					for i2, j2 in [(il-1, jl), (il, jl-1), (il+1, jl), (il, jl+1)]:
						if 0<=i2<height and 0<=j2<width and grid[i2][j2]==1\
						 and (i2, j2) not in seen:
							seen.add((i2, j2))
							to_visit.append((i2, j2))
				island = max(island, shape)
	return island

if __name__ == "__main__":

	grid = [
		[0,0,1,0,0,0,0,1,0,0,0,0,0],
		[0,0,0,0,0,0,0,1,1,1,0,0,0],
		[0,1,1,0,1,0,0,0,0,0,0,0,0],
		[0,1,0,0,1,1,0,0,1,0,1,0,0],
		[0,1,0,0,1,1,0,0,1,1,1,0,0],
		[0,0,0,0,0,0,0,0,0,0,1,0,0],
		[0,0,0,0,0,0,0,1,1,1,0,0,0],
		[0,0,0,0,0,0,0,1,1,0,0,0,0]
	]
	print(max_area_of_island(grid))