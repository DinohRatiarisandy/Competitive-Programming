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
	s = list(s)
	for i, char in enumerate(s):
		if char.islower():
			s[i] = char.upper()
		else:
			s[i] = char.lower()
	return ''.join(s)

if __name__ == "__main__":

	s = inp()
	print(solve(s))