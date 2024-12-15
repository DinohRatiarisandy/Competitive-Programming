# https://codeforces.com/contest/2044/problem/A

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
    cnt = 0
	
    for b in range(1, n):
        a = n - b
        if a+b == n:
            cnt += 1
    return cnt 

if __name__ == "__main__":
    tc = iinp()

    while tc:
        print(solve(iinp()))
        tc -= 1