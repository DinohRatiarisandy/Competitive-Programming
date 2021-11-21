from sys import stdin

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())


def is_valid_bracket_naive(bracket):
	close_bracket = ')]}'

	if len(bracket)==1 or bracket[0] in close_bracket:
		return False

	brack1 = '()'
	brack2 = "{}"
	brack3 = '[]'


	dp = [False for _ in range(len(bracket))]

	for i in range(len(bracket)):
		curr = bracket[i]
		bra_open_close = []
		open_b = ''
		close_b = ''
		opn = clos = 0
		if curr in close_bracket:
			close_b = str(curr)
			clos = i
			for bra in [brack1, brack2, brack3]:
				if close_b in bra:
					bra_open_close = bra
					break
			for j in range(i-1, -1, -1):
				if dp[j]==False:
					open_b = str(bracket[j])
					opn = j
					break
			# print(open_b, close_b)
			if open_b==bra_open_close[0] and close_b==bra_open_close[1]:
				dp[opn] = dp[clos] = True
			else:
				return False
	# print(dp)
	return False if False in dp else True

def is_valid_bracket(bracket):
	close_bracket = ')}]'
	open_bracket  = '({['

	if len(bracket)==1 or len(bracket)%2!=0 or \
	 bracket[0] in close_bracket or bracket[-1] in open_bracket:
		return False

	stack = []

	for i in range(len(bracket)-1, -1, -1):
		current = bracket[i]
		if current in open_bracket:
			if stack:
				if close_bracket.index(stack.pop())==open_bracket.index(current):
					continue
				else:
					return False
			else:
				if current in open_bracket:
					return False
					
		stack.append(current)

	return False if stack else True

if __name__ == "__main__":

	bracket = inp()
	print(is_valid_bracket(bracket))