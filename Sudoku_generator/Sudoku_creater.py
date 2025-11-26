from random import shuffle, randint
from .Sudoku_solver import Solver
from copy import deepcopy



def digging_holes(or_grid: list[list[int]], difficulty: str) -> list[list[int]]:

    match difficulty:
        case 'Easy':
            target = randint(39, 47)
        case 'Medium':
            target = randint(32, 38)
        case "Hard":
            target = randint(26, 31)

    attempts: int = 0
    max_attempts: int = 10

    best_grid = None
    min_clues: int = 81

    while attempts < max_attempts:

        grid = deepcopy(or_grid)

        clues: int = 81

        indexes = [(x, y) for x in range(9) for y in range(9)]
        shuffle(indexes)

        for i, j in indexes:

            if clues == target:
                return grid

            backup = grid[i][j]

            grid[i][j] = 0

            check = Solver(deepcopy(grid))
            if check.counter != 1:
                grid[i][j] = backup
            else:
                clues -= 1
        if clues <= target:
            return grid

        if clues < min_clues:
            best_grid = grid
            min_clues = clues

        attempts += 1

    return best_grid