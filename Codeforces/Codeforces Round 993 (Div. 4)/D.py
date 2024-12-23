# https://codeforces.com/contest/2044/problem/D

from sys import stdin

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())

from sys import stdin, stdout

def solve(n, a):
    seen = set()  # Garde les valeurs déjà utilisées
    available = iter(range(1, n + 1))  # Génère dynamiquement les valeurs disponibles
    sol = []

    for ai in a:
        if ai not in seen:
            sol.append(ai)
            seen.add(ai)
        else:
            # Trouver une nouvelle valeur disponible
            while True:
                candidate = next(available)
                if candidate not in seen:
                    sol.append(candidate)
                    seen.add(candidate)
                    break

    return " ".join(map(str, sol))
    
if __name__ == "__main__":
    tc = iinp()
    
    while tc:
        n = iinp()
        a = liinp()
        print(solve(n, a))
        tc -= 1
