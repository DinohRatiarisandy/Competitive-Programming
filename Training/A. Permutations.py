# https://codeforces.com/group/5tN48zOVvQ/contest/205012/problem/A

def generate_permutation(n, depth=0, seen=set(), curr_perm="", solutions=[]):
	if depth == n:
		solutions.append(curr_perm.rstrip())
		return

	for k in range(1, n+1):
		if k not in seen:
			used = seen.copy()
			used.add(k)
			generate_permutation(n, depth=depth + 1, seen=used, curr_perm=curr_perm+str(k))

	return solutions

if __name__ == "__main__":
	n = int(input())
	
	permutations = generate_permutation(n)

	print("\n".join(permutations))