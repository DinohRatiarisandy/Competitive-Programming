# https://codeforces.com/problemset/problem/1931/C

from sys import stdin

def inp():
    return stdin.readline().rstrip()

def iinp():
    return int(inp())

def mp():
    return map(int, inp().split())

def liinp():
    return list(mp())

def solve(n, array):
    if n == 1:
        return 0

    elif n == 2:
        if array[0] == array[1]:
            return 0
        return 1
    
    idx_left = -1
    idx_right = -1

    # Find idx_left
    for i in range(n-1):
        if array[i] != array[i + 1]:
            idx_left = i
            break
    else:
        return 0
    
    # Find idx_right
    for j in range(n-1, 0, -1):
        if array[j] != array[j - 1]:
            idx_right = j
            break

    middle = (idx_right - idx_left - 1 ) if array[0] == array[-1] else float("Inf")

    return min(n - idx_left - 1, middle, idx_right)

if __name__ == "__main__":
    tc = iinp()
    
    for _ in range(tc):
        n = iinp()
        array = liinp()
        print(solve(n, array))