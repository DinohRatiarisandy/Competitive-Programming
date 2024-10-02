# https://codeforces.com/problemset/problem/2008/D

from sys import stdin

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())

def solve(n, perm, colors):
    dp = [0 for _ in range(n)]
    seen = set()

    for node in perm:
        if node in seen: continue

        cycle = set()

        curr = node
        while curr not in cycle:
            cycle.add(curr)
            curr = perm[curr - 1]
        
        black = 0
        for nd in cycle:
            if colors[nd - 1] == "0":
                black += 1
        
        for nd in cycle:
            dp[nd-1] = black
            seen.add(nd)
                
    return " ".join(list(map(str, dp)))

if __name__ == "__main__":
    tc = iinp()
	
    for _ in range(tc):
        n = iinp()
        perm = liinp()
        colors = inp()
        print(solve(n, perm, colors))