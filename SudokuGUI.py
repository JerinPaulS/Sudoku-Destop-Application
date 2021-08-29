import Tkinter as tk

# --- functions ---

def grid_layout(mW, grid_dim):
    entries = []

    for row in range(grid_dim):
        for col in range(grid_dim):

            entry = tk.Entry(mW, width=3, highlightthickness=1, highlightbackground='#000000')

            pad_y = (0, 0)
            pad_x = (0, 0)

            if (row+1) % 3 == 0 and (row+1) < grid_dim: # skip for last row
                pad_y = (0, 10)

            if (col+1) % 3 == 0 and (col+1) < grid_dim: # skip for last column
                pad_x = (0, 10)

            entry.grid(row=row, column=col, ipadx=5, ipady=5, padx=pad_x, pady=pad_y)

            entries.append(entry)

    return entries

# --- main ---

mW = tk.Tk()
mW.title('Sudoku')

entries = grid_layout(mW, 9)  # send result

mW.mainloop()
