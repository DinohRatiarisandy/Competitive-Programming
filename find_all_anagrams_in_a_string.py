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


def find_anagrams(s, p):
	len_s  = len(s)
	len_p  = len(p)
	s_hash = [0]*26
	p_hash = [0]*26
	res    = []

	for i in range(len_p):
		p_hash[ord(p[i])-97] += 1
		s_hash[ord(s[i])-97] += 1

	if s_hash==p_hash:
		res.append(0)

	left = 1
	for right in range(len_p, len_s):
		s_hash[ord(s[right])-97]  += 1
		s_hash[ord(s[left-1])-97] -= 1

		if p_hash==s_hash:
			res.append(left)

		left += 1

	return res

if __name__=="__main__":

	s = 'cbaebcbacd'
	p = 'abc'
	print(find_anagrams(s, p))