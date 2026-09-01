import pygame


class Drawing:

    def __init__(self, window, simulation_size, control_area, font):
        self.window = window
        self.simulationSize = simulation_size
        self.controlArea = control_area
        self.font = font

    def draw_cells(self, grid):
        for row in range(grid.gridSize):
            for column in range(grid.gridSize):

                if grid.get_cell(row, column) == 1:

                    x = column * grid.cellSize
                    y = row * grid.cellSize

                    pygame.draw.rect(
                        self.window,
                        (240, 240, 240),
                        (x, y, grid.cellSize, grid.cellSize),
                    )

    def draw_grid(self, grid):
        for x in range(0, self.simulationSize, grid.cellSize):
            pygame.draw.line(
                self.window, (35, 35, 35), (x, 0), (x, self.simulationSize)
            )

        for y in range(0, self.simulationSize, grid.cellSize):
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

    def draw_controls(self, controls, generation, simulation_running):
        # Control panel
        pygame.draw.rect(self.window, (20, 20, 20), self.controlArea)

        # Buttons
        self.draw_button(controls.startButton, "Start")

        self.draw_button(controls.stopButton, "Stop")

        self.draw_button(controls.restartButton, "Restart")

        self.draw_button(controls.stepButton, "Step")

        # Generation counter
        generation_text = self.font.render(
            f"Generation: {generation}", True, (255, 255, 255)
        )

        self.window.blit(generation_text, (20, 890))

        # Simulation status
        if simulation_running:
            status = "Running"
        else:
            status = "Stopped"

        status_text = self.font.render(f"Status: {status}", True, (255, 255, 255))

        self.window.blit(status_text, (200, 890))

        # Speed slider
        speed_title = self.font.render("Simulation Speed", True, (255, 255, 255))

        self.window.blit(speed_title, (550, 810))

        # Slider track
        pygame.draw.rect(self.window, (70, 70, 70), controls.slider, border_radius=5)

        # Calculate position of slider handle
        percentage = (controls.slider_max - controls.slider_value) / (
            controls.slider_max - controls.slider_min
        )

        slider_position = int(controls.slider.left + percentage * controls.slider.width)

        # Slider handle
        pygame.draw.circle(
            self.window, (240, 240, 240), (slider_position, controls.slider.centery), 8
        )

        # Speed labels
        slow_text = self.font.render("Slow", True, (180, 180, 180))

        fast_text = self.font.render("Fast", True, (180, 180, 180))

        self.window.blit(slow_text, (520, 845))

        self.window.blit(fast_text, (685, 845))

    def draw_boundary(self, simulation_area):
        pygame.draw.rect(self.window, (255, 255, 255), simulation_area, 1)
