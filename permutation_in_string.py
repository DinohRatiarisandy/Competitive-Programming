from sys import stdin

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())

def solve(s1, s2):
	s1 = list(s1)
	s2 = list(s2)
	s1.sort()
	for i in range(len(s2)):
		k = i+len(s1)
		sort_s2 = s2[i:k]
		sort_s2.sort()
		if sort_s2==s1:
			return True

	return False

if __name__ == "__main__":
	s1 = inp()
	s2 = inp()
	print(solve(s1, s2))