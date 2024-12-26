# https://codeforces.com/problemset/problem/2050/C

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
	count_3 = n.count("3")
	count_2 = n.count("2")
	sum_digits = sum(int(ni) for ni in n)

	for i in range(count_2 + 1):
		for j in range(count_3 + 1):
			if (sum_digits + 2 * i + 6 * j) % 9 == 0:
				return "Yes"
	
	return "No"

if __name__ == "__main__":
	tc = iinp()

	while tc:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
		print(solve(inp()))
		tc -= 1