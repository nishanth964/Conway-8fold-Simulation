class Grid:

    def __init__(self, grid_size, simulation_size):
        self.gridSize = grid_size
        self.cellSize = simulation_size // grid_size

        # 2d Grid 0 - dead, 1 - alive
        self.grid = [[0 for _ in range(self.gridSize)] for _ in range(self.gridSize)]

    def get_cell(self, row, column):
        return self.grid[row][column]

    def set_cell(self, row, column, state):
        self.grid[row][column] = state

    def count_neighbors(self, row, column):
        count = 0

        for row_offset in (-1, 0, 1):
            for column_offset in (-1, 0, 1):

                # Don't count the cell itself
                if row_offset == 0 and column_offset == 0:
                    continue

                neighbor_row = row + row_offset
                neighbor_column = column + column_offset

                # Ignore cells outside the grid
                if (
                    0 <= neighbor_row < self.gridSize
                    and 0 <= neighbor_column < self.gridSize
                ):
                    count += self.grid[neighbor_row][neighbor_column]

        return count

    def next_generation(self):
        next_grid = [[0 for _ in range(self.gridSize)] for _ in range(self.gridSize)]

        for row in range(self.gridSize):
            for column in range(self.gridSize):

                neighbors = self.count_neighbors(row, column)

                if self.grid[row][column] == 1:

                    # Survival: 2 or 3 neighbors
                    if neighbors == 2 or neighbors == 3:
                        next_grid[row][column] = 1

                else:

                    # Birth: exactly 3 neighbors
                    if neighbors == 3:
                        next_grid[row][column] = 1

        self.grid = next_grid

    def screen_to_grid(self, x, y):
        column = x // self.cellSize
        row = y // self.cellSize

        return row, column

    def clear(self):
        self.grid = [[0 for _ in range(self.gridSize)] for _ in range(self.gridSize)]
