from sys import stdin

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())


def smallest_equal(nums):
	sol = []
	for i in range(len(nums)):
		if i%10==nums[i]:
			sol.append(i)

	return min(sol) if sol else -1

if __name__ == "__main__":

	nums = liinp()
	print(smallest_equal(nums))