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


def contains_duplicate(nums):
	sol = Counter(nums)
	for v in sol.values():
		if v >= 2:
			return True
	return False

if __name__ == "__main__":

	nums = liinp()
	print(contains_duplicate(nums))