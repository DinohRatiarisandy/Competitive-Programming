from sys import stdin

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())


def max_distance(colors):
	leng = len(colors)
	distance = float('-inf')
	left = 0
	while left<leng-1:
		right = left+1
		while right<leng:
			if colors[right]!=colors[left]:
				# print(colors[left], colors[right])
				distance = max(distance, right-left)
				# print(distance)
			right += 1
		left += 1
	return distance

if __name__=="__main__":

	colors = [0,1]
	print(max_distance(colors))