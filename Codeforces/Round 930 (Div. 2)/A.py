# https://codeforces.com/contest/1937/problem/A

import math
from sys import stdin

def input():
    return stdin.readline().rstrip()

def int_input():
    return int(input())

def int_map():
    return map(int, input().split())

def list_int():
    return list(int_map())

def solve(n):
    idx = 1
    while idx * 2 <= n:
        idx *= 2
        
    return idx

if __name__ == "__main__":
    for tc in range(int_input()):
        n = int_input()
        print(solve(n))