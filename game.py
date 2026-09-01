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

        self.simulation_running = False
        self.generation = 0
        self.generation_interval = 0.5
        self.generation_timer = 0

        self.font = pygame.font.Font(None, 24)

        # Simulation area
        self.simulationArea = pygame.Rect(
            0, 0, self.simulationSize, self.simulationSize
        )

        self.controlArea = pygame.Rect(
            0, self.simulationSize, self.width, self.controllersSize
        )

        # Buttons
        self.startButton = pygame.Rect(20, 830, 100, 40)

        self.stopButton = pygame.Rect(140, 830, 100, 40)

        self.restartButton = pygame.Rect(260, 830, 100, 40)

        self.stepButton = pygame.Rect(380, 830, 100, 40)

        # Speed slider
        self.slider = pygame.Rect(520, 830, 200, 10)

        self.slider_min = 0.05
        self.slider_max = 1.0
        self.slider_value = 0.5
        self.slider_dragging = False

        # Grid
        self.gridSize = 200
        self.cellSize = self.simulationSize // self.gridSize

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

    def draw_cells(self):

        for row in range(self.gridSize):

            for column in range(self.gridSize):

                if self.get_cell(row, column) == 1:

                    x = column * self.cellSize
                    y = row * self.cellSize

                    pygame.draw.rect(
                        self.window,
                        (240, 240, 240),
                        (x, y, self.cellSize, self.cellSize),
                    )

    def draw_grid(self):

        for x in range(0, self.simulationSize, self.cellSize):

            pygame.draw.line(
                self.window, (35, 35, 35), (x, 0), (x, self.simulationSize)
            )

        for y in range(0, self.simulationSize, self.cellSize):

            pygame.draw.line(
                self.window, (35, 35, 35), (0, y), (self.simulationSize, y)
            )

    def draw_button(self, button, text):

        # Draw button
        pygame.draw.rect(self.window, (50, 50, 50), button, border_radius=6)

        # Draw button border
        pygame.draw.rect(self.window, (90, 90, 90), button, 1, border_radius=6)

        button_text = self.font.render(text, True, (255, 255, 255))

        text_rect = button_text.get_rect(center=button.center)

        self.window.blit(button_text, text_rect)

    def draw_controls(self):

        # Control panel
        pygame.draw.rect(self.window, (20, 20, 20), self.controlArea)

        # Buttons
        self.draw_button(self.startButton, "Start")

        self.draw_button(self.stopButton, "Stop")

        self.draw_button(self.restartButton, "Restart")

        self.draw_button(self.stepButton, "Step")

        # Generation counter
        generation_text = self.font.render(
            f"Generation: {self.generation}", True, (255, 255, 255)
        )

        self.window.blit(generation_text, (20, 890))

        # Simulation status
        if self.simulation_running:
            status = "Running"
        else:
            status = "Stopped"

        status_text = self.font.render(f"Status: {status}", True, (255, 255, 255))

        self.window.blit(status_text, (200, 890))

        # Speed slider
        speed_title = self.font.render("Simulation Speed", True, (255, 255, 255))

        self.window.blit(speed_title, (550, 810))

        # Slider track
        pygame.draw.rect(self.window, (70, 70, 70), self.slider, border_radius=5)

        # Calculate position of slider handle
        percentage = (self.slider_max - self.slider_value) / (
            self.slider_max - self.slider_min
        )

        slider_position = int(self.slider.left + percentage * self.slider.width)

        # Slider handle
        pygame.draw.circle(
            self.window, (240, 240, 240), (slider_position, self.slider.centery), 8
        )

        # Speed labels
        slow_text = self.font.render("Slow", True, (180, 180, 180))

        fast_text = self.font.render("Fast", True, (180, 180, 180))

        self.window.blit(slow_text, (520, 845))

        self.window.blit(fast_text, (685, 845))

    def update_slider(self, x):

        # Keep slider inside its range
        x = max(self.slider.left, min(x, self.slider.right))

        # Convert mouse position to slider value
        percentage = (x - self.slider.left) / self.slider.width

        self.slider_value = self.slider_max - percentage * (
            self.slider_max - self.slider_min
        )

        self.generation_interval = self.slider_value

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

                    if self.startButton.collidepoint(x, y):

                        self.simulation_running = True

                    elif self.stopButton.collidepoint(x, y):

                        self.simulation_running = False

                    elif self.restartButton.collidepoint(x, y):

                        self.simulation_running = False

                        self.grid = [
                            [0 for _ in range(self.gridSize)]
                            for _ in range(self.gridSize)
                        ]

                        self.generation = 0
                        self.generation_timer = 0

                    elif self.stepButton.collidepoint(x, y):

                        self.next_generation()
                        self.generation += 1

                    elif self.slider.collidepoint(x, y):

                        self.slider_dragging = True
                        self.update_slider(x)

                    elif y < self.simulationSize:

                        row, column = self.screen_to_grid(x, y)

                        if self.get_cell(row, column) == 0:

                            self.set_cell(row, column, 1)

                        else:

                            self.set_cell(row, column, 0)

                # Move slider while holding mouse button
                if event.type == pygame.MOUSEMOTION:

                    if self.slider_dragging:

                        self.update_slider(event.pos[0])

                # Stop dragging slider
                if event.type == pygame.MOUSEBUTTONUP:

                    self.slider_dragging = False

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
            self.draw_controls()

            # Simulation boundary
            pygame.draw.rect(self.window, (255, 255, 255), self.simulationArea, 1)

            pygame.display.flip()

        pygame.quit()
