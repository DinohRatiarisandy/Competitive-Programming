# https://codeforces.com/problemset/problem/1927/C

from sys import stdin

def input():
    return stdin.readline().rstrip()

def int_input():
    return int(input())

def int_map():
    return map(int, input().split())

def list_int():
    return list(int_map())

def solve(k, array_a, array_b):
    occurences = [0 for _ in range(k + 1)]

    for a in array_a:
        if a <= k:
            occurences[a] |= 1
        
    for b in array_b:
        if b <= k:
            occurences[b] |= 2
    
    counts = [0 for _ in range(4)]

    for e in occurences:
        counts[e] += 1
    
    if counts[1] > (k // 2) or counts[2] > (k // 2) or sum(counts[1:]) != k:
        return 'NO'

    return 'YES'

if __name__ == "__main__":
    for t in range(int_input()):
        n, m, k = list_int()

        array_a = list_int()
        array_b = list_int()

        print(solve(k, array_a, array_b))