# https://codeforces.com/problemset/problem/2050/B

from sys import stdin

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())

def solve(n, array):
	odd_vals = [array[i] for i in range(1, n, 2)]
	even_vals = [array[i] for i in range(0, n, 2)]
	
	sum_odd, len_odd = sum(odd_vals), len(odd_vals)
	sum_even, len_even = sum(even_vals), len(even_vals)

	if (sum_odd % len_odd == 0
		and sum_even % len_even == 0
		and sum_odd // len_odd == sum_even // len_even
	):
		return "Yes"

	return "No"

if __name__ == "__main__":
	tc = iinp()

	while tc:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
		n = iinp()
		array = liinp()
		print(solve(n, array))
		tc -= 1