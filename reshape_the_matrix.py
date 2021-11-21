from sys import stdin

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())


def solve(mat, r, c):
	data = []
	for i in mat:
		for j in i:
			data.append(j)

	sol = []
	k = 1
	if len(data)//r==c:
		tmp = []
		for i in range(len(data)):
			tmp.append(data[i])		
			if k==c:
				sol.append(tmp)
				tmp = []
				k = 1
				continue
			k += 1

	return sol if sol else mat

if __name__ == "__main__":

	mat = [[1,2,8],[3,4,9]]
	r, c = liinp()
	print(solve(mat, r, c))