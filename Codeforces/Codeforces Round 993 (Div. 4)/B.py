# https://codeforces.com/contest/2044/problem/B

from sys import stdin

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())


def solve(s):
    corres = {
        "w": "w",
        "p": "q",
        "q": "p"
    }

    res = ""
    
    for i in range(len(s)-1, -1, -1):
        res += corres[s[i]]

    return res

if __name__ == "__main__":
    tc = iinp()

    while tc:
        print(solve(inp()))
        tc -= 1