from sys import stdin

def inp():
	return stdin.readline()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())


def lengt_of_longest_substring(s):
	'''
	substring = set()
	length = 0

	for i in range(len(s)):
		for j in range(i, len(s)):
			c = s[j]
			if c in substring:
				length = max(length, len(substring))
				substring.clear()
				break
			else:
				substring.add(c)
				# print(substring)

	return max(length, len(substring))
	'''
	max_len = 0
	seen_char = ''

	for char in s:
		if char not in seen_char:
			seen_char += char
		else:
			seen_char = seen_char[seen_char.index(char)+1 : ] + char

		max_len = max(max_len, len(seen_char))
		
	return max_len

if __name__ == "__main__":

	s = input()
	print(lengt_of_longest_substring(s))