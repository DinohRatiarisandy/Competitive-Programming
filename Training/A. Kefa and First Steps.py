# https://codeforces.com/problemset/problem/580/A

from sys import stdin

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())

def solve(n, seq):
	max_sub_seq = 0
	curr_sub_seq = 1

	for i in range(n-1):
		if seq[i + 1] >= seq[i]:
			curr_sub_seq += 1
		else: 
			max_sub_seq = max(max_sub_seq, curr_sub_seq)
			curr_sub_seq = 1
	
	return max(max_sub_seq, curr_sub_seq)

if __name__ == "__main__":
	n = iinp()
	seq = liinp()

	print(solve(n, seq))