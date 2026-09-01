import pygame


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Conway: 8Fold Simulation")

        # Window
        self.width = 800
        self.height = 950

        self.simulationSize = 800
        self.controllersSize = 150

        self.clock = pygame.time.Clock()

        self.window = pygame.display.set_mode((self.width, self.height))

        self.simulation_running = True
        self.generation = 0
        self.generation_interval = 0.5
        self.generation_timer = 0

        # Simulation Area
        self.simulationArea = pygame.Rect(
            0, 0, self.simulationSize, self.simulationSize
        )

        # Grid
        self.gridSize = 200
        self.cellSize = self.simulationSize // self.gridSize

        # 2d Grid 0- dead, 1 -alive
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

    def draw_cells(self):
        for row in range(self.gridSize):
            for column in range(self.gridSize):

                if self.get_cell(row, column) == 1:

                    x = column * self.cellSize
                    y = row * self.cellSize

                    pygame.draw.rect(
                        self.window,
                        (255, 255, 255),
                        (x, y, self.cellSize, self.cellSize),
                    )

    def draw_grid(self):

        for x in range(0, self.simulationSize, self.cellSize):
            pygame.draw.line(
                self.window, (40, 40, 40), (x, 0), (x, self.simulationSize)
            )

        for y in range(0, self.simulationSize, self.cellSize):
            pygame.draw.line(
                self.window, (40, 40, 40), (0, y), (self.simulationSize, y)
            )

    def run(self):
        self.running = True

        while self.running:
            # Quit handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Time
            delta_time = self.clock.tick(60) / 1000

            # Update simulation
            if self.simulation_running:
                self.generation_timer += delta_time

                if self.generation_timer >= self.generation_interval:
                    self.next_generation()
                    self.generation += 1
                    self.generation_timer -= self.generation_interval

            # Draw
            self.window.fill((10, 10, 10))

            self.draw_cells()
            self.draw_grid()

            # Simulation boundary
            pygame.draw.rect(
                self.window,
                (255, 255, 255),
                self.simulationArea,
                1,
            )

            pygame.display.flip()

    pygame.quit()
