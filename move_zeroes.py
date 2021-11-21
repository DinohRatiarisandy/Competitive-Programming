from sys import stdin

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())


def move_zeroes(nums):
	'''
	non_zeroes =[]
	zeroes = []
	for num in nums:
		if num != 0:
			non_zeroes.append(num)
		else:
			zeroes.append(num)

	nums[:] = non_zeroes+zeroes
	'''
	last_non_zero = 0
	for i in range(len(nums)):
		if nums[i] != 0:
			nums[last_non_zero] = nums[i]
			last_non_zero += 1
	for j in range(last_non_zero, len(nums)):
		nums[j] = 0
	return nums

if __name__ == "__main__":

	nums = liinp()
	print(move_zeroes(nums))