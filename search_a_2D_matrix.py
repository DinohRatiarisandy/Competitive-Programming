from sys import stdin

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())


def search_matrix(matrix, target):
	len_mat = len(matrix)
	j = 0
	k = 1

	for x in range(len_mat):
		if matrix[x][0]<=target<=matrix[x][-1]:
			j = x
			break
		if k==len_mat:
			return False
		k += 1

	i = 0
	while i<len(matrix[j]):
		begin, end = 0, len(matrix[j])-1
		while begin<=end:
			mid = (begin+end)//2
			if matrix[j][mid]==target:
				return True
			elif matrix[j][mid]<target:
				begin = mid+1
			else:
				end = mid-1
		i += 1
	return False

if __name__ == "__main__":

	matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
	target = 16
	print(search_matrix(matrix, target))