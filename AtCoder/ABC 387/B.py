# https://atcoder.jp/contests/abc387/tasks/abc387_b

from sys import stdin

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())

def generate_grid():
	grid = [[i * j for i in range(1, 10)] for j in range(1, 10)]
	
	return grid

def solve(n):
	grid = generate_grid()

	sol = 0

	for i in range(9):
		for j in range(9):
			if grid[i][j] != n:
				sol += grid[i][j]
	
	return sol

if __name__ == "__main__":
	print(solve(iinp()))