# https://codeforces.com/problemset/problem/124/A

from sys import stdin

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())

def solve(n, a, b):
    res = 0

    for i in range(1, n+1):
        if i - 1 <= b and n - i >= a:
            res += 1

    return res

if __name__ == "__main__":
    n, a, b = liinp()
	
    print(solve(n, a, b))