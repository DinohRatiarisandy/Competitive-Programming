from bisect      import bisect_left as bl, bisect_right as br, bisect
from collections import defaultdict as dd, deque, Counter
from heapq       import merge, heapify, heappop, heappush, nsmallest
from itertools   import combinations
from math        import floor, gcd, fabs, factorial, fmod, sqrt, inf, log
from sys         import stdin, stdout

MOD  = pow(10, 9) + 7
MOD2 = 998244353
PI   = 3.141592653589793

# input str
def inp():
    return stdin.readline().strip()

# input int
def iinp():
    return int(inp())

# map and array of int
def mp():
    return map(int, inp().split())

def liinp():
    return list(mp())

# array of string/char
def lmps():
    return map(str, inp().split())

# output (solutions)
def out(var, end="\n"):
    stdout.write(str(var)+end)

def outa(*var, end="\n"):
    stdout.write(' '.join(map(str, var))+end)

# dp
def l1d(n, val=0):
    return [val for i in range(n)]  # dp[i]

def l2d(n, m, val=0):
    return [l1d(m, val) for j in range(n)]  # dp[i][j]

# functions
def DFS(board, pos):
    height  = len(board)
    width   = len(board[0])
    visited = []

    while pos:
        ii, jj        = pos.pop()
        board[ii][jj] = '+'

        for row, col in [(ii-1, jj), (ii+1, jj), (ii, jj-1), (ii, jj+1)]:
            if 0<=row<height and 0<=col<width and (row, col) not in visited\
             and board[row][col]=='O':
                board[row][col] = '+'
                pos.append((row, col))
                visited.append((row, col))

    for row in range(height):
        for col in range(width):
            if board[row][col]=='+':
                board[row][col] = 'O'
            elif board[row][col]=='O':
                board[row][col] = 'X'

    return board

def solve(board):
    pos  = list()
    height = len(board)
    width  = len(board[0])

    if width<3 or height<3:
        return board

    for ii in range(height):
        for jj in range(width):
            if ii==0 or ii==height-1:
                if board[ii][jj]=='O':
                    if (ii, jj) not in pos:
                        pos.append((ii, jj)) 
            if jj==0 or jj==width-1:
                if board[ii][jj]=='O':
                    if (ii, jj) not in pos:
                        pos.append((ii, jj)) 
    if pos:
        return DFS(board, pos)

    else:
        for row in range(height):
            for col in range(width):
                if board[row][col]=='O':
                    board[row][col] = 'X'

        return board

# ----- main() -----
if __name__ == '__main__':

    board = [
        ["O","X"],
        ["O","X"],
        ["O","X"],
        ["X","O"],
    ]

    print(solve(board))
