import pygame


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Conway: 8Fold Simulation")

        # window surface and the display surface
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

    def run(self):
        self.running = True

        # quit handeling
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.window.fill((10, 10, 10))

            # Simulation boundry 
            pygame.draw.rect(self.window, (255, 255, 255), self.simulationArea, 1)

            # Draw on simulation surface
            for x in range(0, self.simulationSize, self.cellSize):
                pygame.draw.line(
                    self.window, (40, 40, 40), (x, 0), (x, self.simulationSize)
                )

            for y in range(0, self.simulationSize, self.cellSize):
                pygame.draw.line(
                    self.window, (40, 40, 40), (0, y), (self.simulationSize, y)
                )

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
