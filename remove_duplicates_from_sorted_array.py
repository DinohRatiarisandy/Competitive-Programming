from sys import stdin

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())


def remove_duplicate(nums):
	if not nums:
		return 0
	slow = 0
	for fast in range(1, len(nums)):
		if nums[slow]!=nums[fast]:
			slow += 1
			nums[slow] = nums[fast]
	return nums[:slow+1]
if __name__ == "__main__":

	nums   = [0,0,1,1,1,2,2,3,3,4,4]
	print(remove_duplicate(nums))