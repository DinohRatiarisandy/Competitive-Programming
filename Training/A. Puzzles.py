# https://codeforces.com/problemset/problem/337/A

from sys import stdin

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())

def solve(n, m, puzzles):
	puzzles.sort()
	sol = float("Inf")

	for i in range(m-n+1):
		seq = puzzles[i : i+n]
		sol = min(sol, seq[-1] - seq[0])
	
	return sol

if __name__ == "__main__":
	n, m = liinp()
	puzzles = liinp()

	print(solve(n, m, puzzles))