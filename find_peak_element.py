from sys import stdin

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())


def find_peak_element(nums):
	start = 0
	end   = len(nums)-1
	while start<end:
		mid = (end+start)//2
		if nums[mid]>nums[mid+1]:
			end = mid
		else:
			start = mid+1

	return start

if __name__ == "__main__":

	nums = liinp()
	print(find_peak_element(nums))