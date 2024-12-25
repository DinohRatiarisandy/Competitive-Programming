"""

Sliding Puzzles
Time limit: 2s. Memory limit: 256MB.

Bessie and her best friend Elsie each own a sliding puzzle. Each of their sliding puzzles consists of
a 2 × 2 grid and three tiles labeled A, B, and C. The three tiles sit on top of the grid, with one
grid cell left empty. To make a move, one slides a tile adjacent to the empty cell into the empty
cell, as shown below:

A B    -->    B
  C         A C

Bessie and Elsie would like to know if there exists a sequence of moves that takes their puzzles to
the same configuration. (Moves can be performed on both puzzles.) Two puzzles are considered
to be in the same configuration if each tile is on top of the same grid cell in both puzzles. Since
the tiles are labeled with letters, rotations and reflections are not allowed.

Input
The first two lines of the input consist of a 2 × 2 grid describing the initial configuration of
Bessie’s puzzle. The next two lines contain a 2 × 2 grid describing the initial configuration of
Elsie’s puzzle. The positions of the tiles are labeled A, B, and C, while the empty cell is labeled X.
It is guaranteed that the input contains two valid descriptions of puzzles.

Output
Print YES if the puzzles can reach the same configuration. Otherwise, print NO.
[Adapted from Codeforces 645A.]

https://codeforces.com/problemset/problem/645/A

"""

from sys import stdin

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())

def solve(bessie, elsie):
	corres = {
		bessie[0]: bessie[1],
		bessie[1]: bessie[2],
		bessie[2]: bessie[0]
	}

	sol = corres[elsie[0]] == elsie[1]

	return "YES" if sol else "NO"

if __name__ == "__main__":
	bessie = ""
	bessie += inp()
	bessie += inp()[::-1]

	elsie = ""
	elsie += inp()
	elsie += inp()[::-1]

	print(solve("".join(bessie.split('X')), "".join(elsie.split('X'))))