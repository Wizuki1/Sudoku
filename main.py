import customtkinter as ct
from Sudoku_generator.Sudoku_transforming import TransformedGrid
from Sudoku_generator.Sudoku_creater import digging_holes
from json import load
from random import choice


def validate(val: str):
    if val == '':
        return True
    elif val.isdigit() and len(val) == 1 and val != "0":
        return True
    return False


def check_answer(event, row: int, col: int, widget: ct.CTkEntry, sol_grid: list[list[int]]):
    value = widget.get()


    if not value:
        widget.configure(fg_color='white')
    elif value == str(sol_grid[row][col]):
        widget.configure(fg_color='#e6efd1')
    else:
        widget.configure(fg_color='#f6c6c5')




def start_screen(root, grid: list[list[int]]):
    """Creates a start screen with difficulties"""
    global start_frame

    start_frame = ct.CTkFrame(root)
    start_frame.pack(fill="both", expand=True)

    title_label = ct.CTkLabel(start_frame, text="Sudoku Game", font=("Roboto", 32, "bold"), text_color="#2e86ab")
    title_label.pack(pady=(40, 20))

    subtitle_label = ct.CTkLabel(start_frame, text="Please choose difficulty", font=("Roboto", 24), text_color="#2e86ab")
    subtitle_label.pack(pady=(0, 40))

    for difficulty in ['Easy', 'Medium', 'Hard']:
        button = ct.CTkButton(start_frame, text=difficulty, font=("Arial", 16), height=55,
                              command=lambda d=difficulty: start_game(root, grid, d))
        button.pack(pady=35, padx=60, fill="x")

def start_game(root, grid: list[list[int]], difficulty: str):
    """Main field with numbers"""

    valid = root.register(validate)

    start_frame.forget()

    grid_frame = ct.CTkFrame(root, fg_color='transparent')
    grid_frame.pack(padx=18, pady=18, fill='both', expand=True)



    gr = digging_holes(grid, difficulty)

    for i in range(9):
        for j in range(9):
            val = gr[i][j]

            cell = ct.CTkEntry(grid_frame, width=60, height=60, justify='center', font=('Roboto', 20), validate="key",
            validatecommand=(valid, "%P"), fg_color='white')
            if not val:
                if i in [2, 5] and j in [2, 5]:
                    cell.grid(row=i, column=j, padx=(0, 4), pady=(0, 4))
                elif j in [2, 5]:
                    cell.grid(row=i, column=j, padx=(0, 4), pady=0)
                elif i in [2, 5]:
                    cell.grid(row=i, column=j, padx=0, pady=(0, 4))
                else:
                    cell.grid(row=i, column=j, padx=0, pady=0)
            else:
                cell.insert(0, str(val))
                cell.configure(state='disabled')
                if i in [2, 5] and j in [2, 5]:
                    cell.grid(row=i, column=j, padx=(0, 4), pady=(0, 4))
                elif j in [2, 5]:
                    cell.grid(row=i, column=j, padx=(0, 4), pady=0)
                elif i in [2, 5]:
                    cell.grid(row=i, column=j, padx=0, pady=(0, 4))
                else:
                    cell.grid(row=i, column=j, padx=0, pady=0)
            cell.bind("<KeyRelease>", lambda event, r=i, c=j, w=cell, g=grid: check_answer(event, r, c, w, g))

def main():
    """Main function which collects all files in one, and creates a GUI"""
    puzzles: list[str] = ['Puzzle_01.json', 'Puzzle_02.json', 'Puzzle_03.json']
    with open(f'Sudoku_generator/puzzles/{choice(puzzles)}') as f:
        matrix: list[list[int]] = load(f)

    grid: list[list[int]] = TransformedGrid(matrix).grid


    root = ct.CTk()
    root.geometry('600x600')
    root.title("Sudoku")

    start_screen(root, grid)

    root.mainloop()


if __name__ == '__main__':
    main()