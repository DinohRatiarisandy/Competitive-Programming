# https://codeforces.com/problemset/problem/2041/E

from sys import stdin

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())

if __name__ == "__main__":
	a, b = liinp()

	print(3)
	print(f"{b} {b} {3*a - 2*b}")
