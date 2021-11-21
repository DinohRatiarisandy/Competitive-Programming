from sys import stdin

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())


def pascal_triangle(num_row):
	pascal_triangle = [[1], [1, 1]]
	k = 1
	if num_row==1:
		return [[1]]
		
	while num_row>0 and num_row>2:
		tmp = [0 for _ in range(len(pascal_triangle[k])+1)]
		j = 1
		for i in range(len(pascal_triangle[k])-1):
			tmp[j] = pascal_triangle[k][i]+pascal_triangle[k][i+1]
			j += 1
		tmp[0] = 1
		tmp[-1] = 1
		pascal_triangle.append(tmp)
		k += 1
		num_row -= 1

	return pascal_triangle

if __name__ == "__main__":

	num_row = iinp()
	print(pascal_triangle(num_row))