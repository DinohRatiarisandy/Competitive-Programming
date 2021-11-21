from sys import stdin

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())


def backspace_compare(s, t):
	stack_s = []
	stack_t = []
	for c in s:
		if c!='#':
			stack_s.append(c)
		else:
			if stack_s:
				stack_s.pop()
			else: continue

	for c in t:
		if c!='#':
			stack_t.append(c)
		else:
			if stack_t:
				stack_t.pop()
			else: continue

	return stack_s==stack_t

if __name__ == "__main__":

	# s = inp()
	# t = inp()
	s = "a"
	t = "a#"
	print(backspace_compare(s, t))