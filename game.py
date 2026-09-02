import pygame

from controls import Controls
from drawing import Drawing
from grid import Grid


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

        self.simulation_running = False
        self.generation = 0
        self.generation_interval = 0.5
        self.generation_timer = 0

        self.is_drawing = False
        self.last_drawn_cell = None

        self.font = pygame.font.Font(None, 24)

        # Simulation area
        self.simulationArea = pygame.Rect(
            0, 0, self.simulationSize, self.simulationSize
        )

        self.controlArea = pygame.Rect(
            0, self.simulationSize, self.width, self.controllersSize
        )

        # Grid
        self.grid = Grid(200, self.simulationSize)

        # Controls
        self.controls = Controls()

        # Drawing
        self.drawing = Drawing(
            self.window, self.simulationSize, self.controlArea, self.font
        )

    def restart(self):

        self.simulation_running = False
        self.grid.clear()
        self.generation = 0
        self.generation_timer = 0

    def run(self):

        self.running = True

        while self.running:

            # Quit handling
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False

                # Mouse handling
                if event.type == pygame.MOUSEBUTTONDOWN:

                    x, y = event.pos

                    if self.controls.startButton.collidepoint(x, y):
                        self.simulation_running = True

                    elif self.controls.stopButton.collidepoint(x, y):
                        self.simulation_running = False

                    elif self.controls.restartButton.collidepoint(x, y):
                        self.restart()

                    elif self.controls.stepButton.collidepoint(x, y):
                        self.grid.next_generation()
                        self.generation += 1

                    elif self.controls.slider.collidepoint(x, y):
                        self.controls.slider_dragging = True

                        self.generation_interval = self.controls.update_slider(x)

                    elif y < self.simulationSize:

                        row, column = self.grid.screen_to_grid(x, y)

                        self.is_drawing = True
                        self.last_drawn_cell = (row, column)

                        if self.grid.get_cell(row, column) == 0:

                            self.grid.set_symmetric_cell(row, column, 1)

                        else:

                            self.grid.set_symmetric_cell(row, column, 0)

                # Move slider or draw while holding mouse button
                if event.type == pygame.MOUSEMOTION:

                    if self.controls.slider_dragging:

                        self.generation_interval = self.controls.update_slider(
                            event.pos[0]
                        )

                    elif self.is_drawing:

                        x, y = event.pos

                        if y < self.simulationSize:

                            row, column = self.grid.screen_to_grid(x, y)

                            current_cell = (row, column)

                            if current_cell != self.last_drawn_cell:

                                self.grid.set_symmetric_cell(row, column, 1)

                                self.last_drawn_cell = current_cell

                # Stop dragging slider or drawing
                if event.type == pygame.MOUSEBUTTONUP:

                    self.controls.slider_dragging = False
                    self.is_drawing = False
                    self.last_drawn_cell = None

            # Time
            delta_time = self.clock.tick(60) / 1000

            # Update simulation
            if self.simulation_running:

                self.generation_timer += delta_time

                if self.generation_timer >= self.generation_interval:

                    self.grid.next_generation()
                    self.generation += 1

                    self.generation_timer -= self.generation_interval

            # Draw
            self.window.fill((10, 10, 10))

            self.drawing.draw_cells(self.grid)

            self.drawing.draw_grid(self.grid)

            self.drawing.draw_controls(
                self.controls, self.generation, self.simulation_running
            )

            self.drawing.draw_boundary(self.simulationArea)

            pygame.display.flip()

        pygame.quit()
