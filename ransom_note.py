from sys import stdin

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())


def solve(ransom_note, magazine):
	for char in set(ransom_note):
		if magazine.count(char) < ransom_note.count(char):
			return False
	return True

if __name__ == "__main__":

	ransom_note = inp()
	magazine = inp()
	print(solve(ransom_note, magazine))