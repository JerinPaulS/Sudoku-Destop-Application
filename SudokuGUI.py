import Tkinter as tk

def grid_layout(win, grid_dim):
    entries = []

    for row in range(grid_dim):
        for col in range(grid_dim):
            if question[row][col] == ".":
                entry = tk.Entry(win, width = 3, font=("Calibri 10"), justify = 'center')
            else:
                val = tk.StringVar()
                entry = tk.Entry(win, width = 3, font=("Calibri 10"), textvariable = val, state = tk.DISABLED, justify = 'center')
                val.set(question[row][col])
            pad_y = (0, 0)
            pad_x = (0, 0)
            if (row + 1) % 3 == 0 and (row + 1) < grid_dim:
                pad_y = (0, 3)
            if (col + 1) % 3 == 0 and (col + 1) < grid_dim:
                pad_x = (0, 3)
            entry.grid(row = row, column = col, ipadx = 15, ipady = 15, padx = pad_x, pady = pad_y)
            entries.append(entry)
    return entries

def start_func():
    return 0

def clear_func():
    return 0

def solveSudoku():
    board = question
    if solve(0, 0, board):
        return board

def solve(row, col, board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                for c in range(1, 10):
                    if isvalid(i, j, str(c), board):
                        board[i][j]= str(c)
                        if solve(row, col, board) == True:
                            return True
                        board[i][j] = '.'
                return False
    return True

def isvalid(row, col, c, board):
    for i in range(9):
        if board[i][col] == c:
            return False
        if board[row][i] == c:
            return False
        if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == c:
            return False
    return True

question = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

win = tk.Tk()
win.minsize(550, 530)
win.maxsize(550, 530)
win.title('Sudoku')
entries = grid_layout(win, 9)

button1 = tk.Button(win, width = 3, text = "Start", command = start_func)
button1.grid(row = 15, column = 1)

button2 = tk.Button(win, width = 3, text = "Clear", command = clear_func)
button2.grid(row = 15,column = 3)

button3 = tk.Button(win, width = 3, text = "Solve", command = solveSudoku)
button3.grid(row = 15,column = 5)

timer = tk.Entry(win, width = 5)
timer.grid(row = 15, column = 7)

win.mainloop()
