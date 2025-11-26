from copy import deepcopy

class Solver:
    """Solving sudoku and counting number of valid solutions"""
    def __init__(self, grid: list[list[int]]):
        self.counter = 0
        self.grid = deepcopy(grid)
        self.__solve()

    def __find_empty(self):
        """Finds if cell is empty"""
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    return i, j
        return None




    def __is_valid(self, row: int, column: int, num: int):
        """Checks if num is valid"""

        for i in range(9):
            if self.grid[row][i] == num:
                return False

        for i in range(9):
            if self.grid[i][column] == num:
                return False

        start_row = (row // 3) * 3
        start_col = (column // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.grid[start_row + i][start_col + j] == num:
                    return False

        return True

    def __solve(self):
        """Recursively solves the sudoku"""
        if not self.__find_empty():
            self.counter += 1
            return
        if self.counter > 1:
            return

        row, column = self.__find_empty()

        for i in range(1, 10):
            if self.__is_valid(row, column, i):
                self.grid[row][column] = i
                self.__solve()
                self.grid[row][column] = 0