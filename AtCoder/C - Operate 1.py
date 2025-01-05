# https://atcoder.jp/contests/abc386/tasks/abc386_c

from sys import stdin

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())

def solve(S, T):
	len_S, len_T = len(S), len(T)

	if abs(len_S - len_T) > 1:
		return "No"
	
	if len_S == len_T:
		diff = sum(1 for a, b in zip(S, T) if a != b)
		return "Yes" if diff <= 1 else "No"
	
	if len_S < len_T:
		i, j = 0, 0
		mismatch = 0
		while i < len_S and j < len_T:
			if S[i] != T[j]:
				mismatch += 1
				if mismatch > 1:
					return "No"
				j += 1
			else:
				i += 1
				j += 1
		return "Yes"

	else:
		i, j = 0, 0
		mismatch = 0
		while i < len_S and j < len_T:
			if S[i] != T[j]:
				mismatch += 1
				if mismatch > 1:
					return "No"
				i += 1
			else:
				i += 1
				j += 1
		return "Yes"


if __name__ == "__main__":
	K = iinp()
	S = inp()
	T = inp()
	print(solve(S, T))