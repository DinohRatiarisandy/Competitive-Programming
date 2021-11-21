from sys import stdin
from collections import Counter

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())


def solve(strg):
	char_freq = Counter(strg)
	for char, freq in char_freq.items():
		if freq==1:
			return strg.index(char)
	return -1

if __name__ == "__main__":

	strg = inp()
	print(solve(strg))