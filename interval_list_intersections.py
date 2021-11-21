from sys import stdin

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())


def solve(first_list, second_list):
	intersection = []
	i = j = 0
	if first_list and second_list:
		while i<len(first_list) and j<len(second_list):
			a_start, a_end = first_list[i]
			b_start, b_end = second_list[j]
			if a_start<=b_end and b_start<=a_end:
				intersection.append([max(a_start, b_start), min(a_end, b_end)])
			if a_end==b_end:
				i += 1
				j += 1
			elif a_end<b_end:
				i += 1

			else:
				j += 1
	return intersection
if __name__ == "__main__":

	first_list  = [[0,2],[5,10],[13,23],[24,25]]
	second_list = [[1,5],[8,12],[15,24],[25,26]]
	print(solve(first_list, second_list))