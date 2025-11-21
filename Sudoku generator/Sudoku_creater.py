from random import shuffle, randint
from Sudoku_solver import Solver
from copy import deepcopy

def digging_holes(grid: list[list[int]], difficulty: str) -> list[list[int]]:
    indexes = [(x, y) for x in range(9) for y in range(9)]
    shuffle(indexes)

    match difficulty:
        case 'Easy':
            target = randint(39, 47)
        case 'Medium':
            target = randint(32, 38)
        case "Hard":
            target = randint(26, 31)
        case "Exteme":
            target = randint(21, 25)
    clues: int = 81

    for i, j in indexes:

        if clues == target:
            break

        backup = grid[i][j]

        grid[i][j] = 0

        check = Solver(deepcopy(grid))
        if check.counter != 1:
            grid[i][j] = backup
        else:
            clues -= 1

    return grid