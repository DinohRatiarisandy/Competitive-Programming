from sys import stdin

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())


def max_area(nums):
	max_area_water = float('-Inf')
	left, right = 0, len(nums)-1
	while left<right:
		max_area_water = max(max_area_water, min(nums[left], nums[right])*(right-left))
		if nums[left]<nums[right]:
			left += 1
		else:
			right -= 1
	return max_area_water

if __name__ == "__main__":

	nums = [1,8,6,2,5,4,8,3,7]
	print(max_area(nums))