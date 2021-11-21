from sys import stdin

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())

def is_valid_row(row, board):
	current_row = board[row]

	# remove all '.'
	current_row = list(filter(lambda a: a!='.', current_row))

	if any(int(i)<0 and int(i)>9 for i in current_row if i!='.'):
		return False

	elif len(current_row)!=len(set(current_row)):
		return False

	return True

def is_valid_col(col, board):
	current_col = [row[col] for row in board]

	# remove all '.'
	current_col = list(filter(lambda a: a!='.', current_col))

	if any(int(i)<0 and int(i)>9 for i in current_col if i!='.'):
		return False

	elif len(current_col)!=len(set(current_col)):
		return False

	return True

def is_valid_subsquares(board):
	for row in range(0, 9, 3):
		for col in range(0, 9, 3):
			tmp = []
			for r in range(row, row+3):
				for c in range(col, col+3):
					if board[r][c] != '.':
						tmp.append(board[r][c])
				if any(int(i)<0 and int(i)>9 for i in tmp):
					return False
				elif len(tmp)!=len(set(tmp)):
					return False
	return True

def is_valid_sudoku(board):
	for i in range(9):
		validate_row = is_valid_row(i, board)
		validate_col = is_valid_col(i, board)
		validate_subsquares = is_valid_subsquares(board)
		
		if False in(validate_col, validate_row, validate_subsquares):
			return False


	return True

if __name__ == "__main__":

	board = \
	[["5","3",".",".","7",".",".",".","."]
	,["6",".",".","1","9","5",".",".","."]
	,[".","9","8",".",".",".",".","6","."]
	,["8",".",".",".","6",".",".",".","3"]
	,["4",".",".","8",".","3",".",".","1"]
	,["7",".",".",".","2",".",".",".","6"]
	,[".","6",".",".",".",".","2","8","."]
	,[".",".",".","4","1","9",".",".","5"]
	,[".",".",".",".","8",".",".","7","5"]]

	print(is_valid_sudoku(board))