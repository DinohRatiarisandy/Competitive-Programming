from sys import stdin

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())


def dfs_grid(image, sr, sc, new_color):
	height = len(image)
	width = len(image[0])
	to_visit = [(sr, sc)]
	old_color = image[sr][sc]
	image[sr][sc] = new_color
	seen = [[False for i in range(width)] for j in range(height)]
	seen[sr][sc] = True

	while to_visit:
		il, jl = to_visit.pop()
		for i2, j2 in [(il+1, jl), (il, jl+1),
						(il, jl-1), (il-1, jl)]:
			if (0 <= i2 < height and 0 <= j2 < width \
					and image[i2][j2]==old_color \
					and seen[i2][j2]==False):
				seen[i2][j2] = True
				image[i2][j2] = new_color
				to_visit.append((i2, j2))

	return image

if __name__ == "__main__":
	image = [[1,1,1],[1,1,0],[1,0,1]]
	sr = 1; sc = 1
	new_color = 2
	print(dfs_grid(image, sr, sc, new_color))