from sys import stdin
from itertools import product

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())

res = []
def backtracking(sub="", i=0):
	# print(sub, len(word))
	if len(sub)==len(word):
		res.append(sub)
	else:
		if word[i].isalpha():
			backtracking(sub+(word[i]).swapcase(), i+1)
		backtracking(sub+(word[i]), i+1)
	return res

def solve(word):
	return backtracking()


if __name__ == "__main__":

	word = inp()
	print(solve(word))
	# Another solution
	print(list(map(''.join, product(*(set([ch.lower(), ch.upper()]) for ch in word)))))