from sys import stdin

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())


def solve(arr, target):
	start = 0
	end   = len(nums)-1
	while start<=end:
		mid = (start+end)//2

		if nums[mid]==target:
			return mid

		if nums[mid]>=nums[start]:
			if nums[start]<=target<nums[mid]:
				end = mid-1
			else:
				start = mid+1
		if nums[mid]<=nums[start]:
			if nums[mid]<=target<nums[end]:
				start = mid+1
			else:
				end = mid-1

	return -1

if __name__ == "__main__":

	nums = liinp()
	target = iinp()
	print(solve(nums, target))