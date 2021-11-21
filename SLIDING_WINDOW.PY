def min_window(s, req_chars):

	# hash to keep account of how many required characters we've checked off
	# each key will represent a character in req_chars
	# we preset each to 1 and will look to lower it to 0 when each is fulfilled

	hash = {}
	for c in req_chars:
		hash[c] = 1

	# trackers that we need
	# this is a counter to measure string length against

	counter = len(req_chars)
	begin = 0
	end = 0
	substr_size = len(s)+1
	head = 0

	while end < len(s):
		# print(f"begin:{s[begin]}, end:{s[end]}")
		# continue running while there's more elements in `s` to process
		if s[end] in hash:  # we've found a letter we needed to fulfill

			# modify the length counter, we can use this as part of our substring
			if hash[s[end]]>0:
				counter -= 1

			# modify the dictionary to say we've gotten this character requirement
			hash[s[end]] -= 1

		# from here, we increase begin pointer to make it invalid/valid again

		while counter==0:  # valid, we have what we need

			# calculate the current substring size since we care about min

			if end-begin+1<substr_size:
				substr_size = end-begin+1
				head = begin

			# we want to shrink it from the beginning now
			# to make it the minimum size possible

			if s[begin] in hash:
				hash[s[begin]] += 1

				# this is a character we need

				if hash[s[begin]] > 0:
					counter += 1  # make it invalid
			begin += 1

		# Keep expanding the window once we are done contracting, try more substrings

		end += 1

	return "" if substr_size==float("inf") else s[head : head+substr_size]

def max_sub_array_of_size_k(arr, k):
	max_sum    = float("-inf")
	window_sum = 0
	start      = 0
	for end in range(len(arr)):
		window_sum += arr[end]
		if end>=k-1:
			max_sum     = max(max_sum, window_sum)
			window_sum -= arr[start]
			start      += 1

	return max_sum

def min_sub_array_len(nums, target):
	min_sum 	= float('inf')
	sum_window  = 0
	start 	    = 0
	for end in range(len(nums)):
		sum_window += nums[end]
		if nums[end]==target:
			return 1
		while sum_window>=target:
			min_sum 	= min(min_sum, end-start+1)
			sum_window -= nums[start]
			start 	   += 1
	return min_sum if min_sum<float('inf') else 0

def num_sub_array_product_less_than_k(nums, k):
	res = 0
	if k>1:
		start   = 0
		product = 1
		for end, val in enumerate(nums):
			product *= val

			while product>=k:
				product /= nums[start]
				start += 1
			res += end-start+1
	return res

if __name__=="__main__":
	arr = [1,1,1]
	k   = 1
	print(num_sub_array_product_less_than_k(arr, k))
	# print (max_sub_array_of_size_k(arr, k))
	# print(min_window("abcalgosodmeilyr", "ad"))


