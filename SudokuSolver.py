class SudokuSolver(object):
	def solveSudoku(self, board):
		if self.solve(0, 0, board):
			return board

	def solve(self, row, col, board):
		for i in range(9):
			for j in range(9):
				if board[i][j] == '.':
					for c in range(1, 10):
						if self.isvalid(i, j, str(c), board):
							board[i][j]= str(c)
							if self.solve(row, col, board) == True:
								return True
							board[i][j] = '.'
					return False
		return True

	def isvalid(self, row, col, c, board):
		for i in range(9):
			if board[i][col] == c:
				return False
			if board[row][i] == c:
				return False
			if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == c:
				return False
		return True

obj = SudokuSolver()
print(obj.solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
