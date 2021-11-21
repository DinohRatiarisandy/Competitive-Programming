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
	dict_nums = dict()
	for i in range(len(nums)):
	    num = nums[i]
	    value = target - num
	    if value in dict_nums:
	        return dict_nums[value], i
	    else:
	        dict_nums[num] = i
	        

if __name__ == "__main__":

	nums = liinp()
	target = iinp()
	print(solve(nums, target))