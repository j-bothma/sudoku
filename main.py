from tkinter import *

root = Tk()
root.title('Sudoku')
root.geometry('1000x1000')

# create all of the main containers
center = Frame(root, bg='white', width=900, height=900, padx=3, pady=3)

# layout all of the main containers
root.grid_rowconfigure(9, weight=1)
root.grid_columnconfigure(9, weight=1)
center.grid(row=1, sticky="nsew")

cells = {}
for row in range(9):
    for column in range(9):
        cell = Frame(center, bg='white', highlightbackground="black",
                     highlightcolor="black", highlightthickness=1,
                     width=100, height=100,  padx=3,  pady=3)
        cell.grid(row=row, column=column)
        cells[(row, column)] = cell

root.mainloop()