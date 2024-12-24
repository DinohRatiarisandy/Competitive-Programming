# https://codeforces.com/problemset/problem/2040/B

from sys import stdin

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())

def solve(n):
	sol = 1
	curr = 1

	while True:
		if curr >= n:
			return sol

		sol += 1
		curr = curr * 2 + 2

if __name__ == "__main__":
	tc = iinp()

	while tc:
		n = iinp()
		print(solve(n))
		tc -= 1