from sys import stdin

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())


def solve(nums):
	'''
	start_value = 1
	while True:
		s = start_value
		for val in nums:
			s = s+val
			if s<1:
				break
		if s<1:
			start_value += 1
		else:
			return start_value
	'''
	n, m = len(nums), 101
	left, right = 1, m
	while left<right:
		total = middle = (right+left)//2
		is_valid = True
		for num in nums:
			total += num
			if total<1:
				is_valid = False

		if is_valid:
			right = middle
		else:
			left = middle+1

	return left


if __name__ == "__main__":

	nums = [-3,2,-3,4,2]
	print(solve(nums))