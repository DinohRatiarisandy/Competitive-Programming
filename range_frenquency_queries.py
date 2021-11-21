from collections import defaultdict
from bisect import bisect_left, bisect_right

def query(arr, left, right, value):
	hash = defaultdict(list)
	for k, val in enumerate(arr):
		hash[val].append(k)

	left_pos  = bisect_left(hash[value], left)
	right_pos = bisect_right(hash[value], right)

	return right_pos-left_pos


if __name__=="__main__":

	nums = [12, 33, 4, 56, 33, 2, 34, 33, 22, 12, 34, 33]
	print(query(nums, 0, 11, 33))