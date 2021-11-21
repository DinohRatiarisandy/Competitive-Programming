from sys import stdin

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())

def solve(nums, target):
	start, end = 0, len(nums)-1
	while start <= end:
		mil = start + (end-start)//2

		if nums[mil]==target:
			return mil	
		if target < nums[mil]:
			end = mil - 1
		elif target > nums[mil]:
			start = mil + 1

	return -1

if __name__ == "__main__":
	nums = liinp()
	target = iinp()
	print(solve(nums, target))