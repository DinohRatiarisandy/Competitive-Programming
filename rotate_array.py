from sys import stdin

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())


def rotate_array(array, k):
	n = len(array)
	# while k:
	# 	print(array)
	# 	first = array[-1]
	# 	for i in range(n-1, 0, -1):
	# 		array[i] = array[i-1]
	# 	array[0] = first

	# 	k -= 1

	i = k%len(array)
	array[:] = array[n-i:]+array[:n-i]
	return array

if __name__ == "__main__":
 
	array = liinp()
	k 	  = iinp()
	print(rotate_array(array, k))