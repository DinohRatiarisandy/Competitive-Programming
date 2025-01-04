# https://atcoder.jp/contests/abc387/tasks/abc387_d

from sys import stdin
from collections import deque

def inp():
    return stdin.readline().rstrip()

def iinp():
    return int(inp())

def mp():
    return map(int, inp().split())

def liinp():
    return list(mp())

def find_s_idx(h, w, grid):
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 'S':
                return (i, j)

def solve(h, w, grid):
    s_idx = find_s_idx(h, w, grid)

    # Structure pour stocker les cellules visitées avec une direction donnée
    visited = [[{"v": False, "h": False} for _ in range(w)] for _ in range(h)]

    # Initialisation de la pile
    stack = deque([(s_idx, "beging", 0)])

    while stack:
        (r, c), last_dir, step = stack.popleft()

        # Si on atteint l'objectif
        if grid[r][c] == 'G':
            return step

        # Liste des mouvements possibles
        moves = []
        if last_dir == 'v':  # Mouvement vertical précédent, autoriser horizontal
            moves = [(r, c + 1, 'h'), (r, c - 1, 'h')]
        elif last_dir == 'h':  # Mouvement horizontal précédent, autoriser vertical
            moves = [(r - 1, c, 'v'), (r + 1, c, 'v')]
        else:  # Départ, autoriser toutes les directions
            moves = [(r - 1, c, 'v'), (r + 1, c, 'v'), (r, c + 1, 'h'), (r, c - 1, 'h')]

        # Parcourir les mouvements possibles
        for nr, nc, new_dir in moves:
            if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] != '#':
                # Vérifier si la cellule n'a pas été visitée dans cette direction
                if not visited[nr][nc][new_dir]:
                    visited[nr][nc][new_dir] = True
                    stack.append(((nr, nc), new_dir, step + 1))

    return -1  # Si aucun chemin n'est trouvé

if __name__ == "__main__":
    h, w = liinp()
    grid = [inp() for _ in range(h)]
    print(solve(h, w, grid))
