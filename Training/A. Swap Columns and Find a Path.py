# https://codeforces.com/problemset/problem/2046/A

from sys import stdin

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())

def solve(n, row_1, row_2):
	total_cost = sum(max(row_1[j], row_2[j]) for j in range(n))
	max_cost = float("-Inf")

	for k in range(n):
		top, bottom = row_1[k], row_2[k]
		curr_cost = total_cost - max(top, bottom) + (top + bottom)
		max_cost = max(curr_cost, max_cost)
	
	return max_cost

if __name__ == "__main__":
	tc = iinp()

	while tc:
		n = iinp()
		row_1 = liinp()
		row_2 = liinp()
		print(solve(n, row_1, row_2))
		tc -= 1