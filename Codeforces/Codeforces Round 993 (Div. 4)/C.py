# https://codeforces.com/contest/2044/problem/C

from sys import stdin

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())


def solve(m, a, b, c):
    row_1 = m - a if (m - a) > 0 else 0
    row_2 = m - b if (m - b) > 0 else 0
    row_3 = (row_1  + row_2) - c if (row_1 + row_2) > 0 and ((row_1  + row_2) - c) > 0 else 0

    return 2*m - row_3

if __name__ == "__main__":
    tc = iinp()

    while tc:
        m, a, b, c = liinp()
        print(solve(m, a, b, c))
        tc -= 1