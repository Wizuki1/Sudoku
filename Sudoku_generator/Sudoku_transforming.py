from random import choice, randint, sample
from copy import deepcopy

class TransformedGrid:
    """Creating a transformed grid"""
    def __init__(self, matrix: list[list[int]]):
        self.grid = deepcopy(matrix)
        self.__random_transforms()

    def __transposition(self):
        """Transpose grid"""
        self.grid = [list(row) for row in zip(*self.grid)]

    def __swap_rows(self):
        """Swaps different rows in 1 region"""
        region_num = randint(0, 2) * 3
        num_row_1, num_row_2 = sample([0, 1, 2], 2)
        index1 = region_num + num_row_1
        index2 = region_num + num_row_2
        self.grid[index1], self.grid[index2] = self.grid[index2], self.grid[index1]

    def __swap_columns(self):
        """Swaps different columns in 1 region"""
        self.__transposition()
        self.__swap_rows()
        self.__transposition()

    def __swap_rows_region(self):
        """swaps whole region (rows)"""
        reg_ind1, reg_ind2 = sample([0, 3, 6], 2)
        self.grid[reg_ind1:reg_ind1 + 3], self.grid[reg_ind2: reg_ind2 + 3] = \
            self.grid[reg_ind2: reg_ind2 + 3], self.grid[reg_ind1:reg_ind1 + 3]

    def __swap_columns_region(self):
        """swaps whole region (columns)"""
        self.__transposition()
        self.__swap_rows_region()
        self.__transposition()

    def __swap_nums(self):
        """swaps nums in the grid"""
        num1, num2 = sample(range(1, 10), 2)
        for i in range(9):
            ind1 = self.grid[i].index(num1)
            ind2 = self.grid[i].index(num2)
            self.grid[i][ind1], self.grid[i][ind2] = self.grid[i][ind2], self.grid[i][ind1]

    def __random_transforms(self):
        """Applying random operation to the grid"""
        funcs = [self.__swap_nums,
                 self.__swap_columns_region,
                 self.__swap_rows_region,
                 self.__swap_columns,
                 self.__swap_rows,
                 self.__transposition]
        for i in range(randint(50, 100)):
            func = choice(funcs)
            func()