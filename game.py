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

        # Drawing state
        self.is_drawing = False
        self.last_drawn_cell = None

        # Font
        self.font = pygame.font.Font(None, 24)

        # Simulation area
        self.simulationArea = pygame.Rect(
            0, 0, self.simulationSize, self.simulationSize
        )

        # Control area
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

    def handle_mouse_down(self, event):

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

        elif self.controls.slider_area.collidepoint(x, y):

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

    def handle_mouse_motion(self, event):

        x, y = event.pos

        if self.controls.slider_dragging:

            self.generation_interval = self.controls.update_slider(x)

        elif self.is_drawing:

            if y < self.simulationSize:

                row, column = self.grid.screen_to_grid(x, y)

                current_cell = (row, column)

                if current_cell != self.last_drawn_cell:

                    self.grid.set_symmetric_cell(row, column, 1)

                    self.last_drawn_cell = current_cell

    def handle_mouse_up(self):

        self.controls.slider_dragging = False
        self.is_drawing = False
        self.last_drawn_cell = None

    def handle_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                self.running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:

                self.handle_mouse_down(event)

            elif event.type == pygame.MOUSEMOTION:

                self.handle_mouse_motion(event)

            elif event.type == pygame.MOUSEBUTTONUP:

                self.handle_mouse_up()

    def update(self, delta_time):

        if not self.simulation_running:
            return

        self.generation_timer += delta_time

        while self.generation_timer >= self.generation_interval:

            self.grid.next_generation()

            self.generation += 1

            self.generation_timer -= self.generation_interval

    def draw(self):

        self.window.fill((5, 5, 8))

        self.drawing.draw_cells(self.grid, self.generation)

        self.drawing.draw_grid(self.grid)

        self.drawing.draw_controls(
            self.controls, self.generation, self.simulation_running
        )

        self.drawing.draw_boundary(self.simulationArea)

        pygame.display.flip()

    def run(self):

        self.running = True

        while self.running:

            self.handle_events()

            delta_time = self.clock.tick(60) / 1000

            self.update(delta_time)

            self.draw()

        pygame.quit()
