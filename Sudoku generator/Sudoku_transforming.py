from random import choice, randint, sample
from json import load

class TransformedGrid:
    """Creating a transformed grid"""
    def __init__(self, matrix: list[list[int]]):
        self.grid = matrix
        self.__swapping_rows(3)

    def __transposition(self):
        """Transpose grid"""
        self.grid = [list(row) for row in zip(*self.grid)]

    def __swapping_rows(self):
        """Swaps different rows in 1 region"""
        region_num = randint(0, 2) * 3
        num_row_1, num_row_2 = sample([0, 1, 2], 2)
        index1 = region_num + num_row_1
        index2 = region_num + num_row_2
        self.grid[index1], self.grid[index2] = self.grid[index2], self.grid[index1]

with open('puzzles\\Puzzle_01.json') as f:
    matrix = load(f)
    for i in matrix:
        print(i)
    matrix = TransformedGrid(matrix).grid

    print('\n------------------------\n')
    for i in matrix:
        print(i)