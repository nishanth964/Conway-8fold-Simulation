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

        # Simulation Area
        self.simulationArea = pygame.Rect(
            0, 0, self.simulationSize, self.simulationSize
        )

        # Grid
        self.gridSize = 200
        self.cellSize = self.simulationSize // self.gridSize

        # 2d Grid 0- dead, 1 -alive
        self.grid = [[0 for _ in range(self.gridSize)] for _ in range(self.gridSize)]

        # Test alive cell
        self.set_cell(10, 20, 1)

    def get_cell(self, row, column):
        return self.grid[row][column]

    def set_cell(self, row, column, state):
        self.grid[row][column] = state

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

        # quit handeling
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.window.fill((10, 10, 10))

            self.draw_cells()
            self.draw_grid()

            # Simulation boundary
            pygame.draw.rect(self.window, (255, 255, 255), self.simulationArea, 1)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
