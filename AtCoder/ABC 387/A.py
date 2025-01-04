# https://atcoder.jp/contests/abc387/tasks/abc387_a

from sys import stdin

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())

def solve(a, b):
	return (a + b) ** 2

if __name__ == "__main__":
    a, b = liinp()
	
    print(solve(a, b))