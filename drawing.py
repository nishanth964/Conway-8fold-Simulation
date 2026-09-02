import math

import pygame


class Drawing:

    def __init__(self, window, simulation_size, control_area, font):
        self.window = window
        self.simulationSize = simulation_size
        self.controlArea = control_area
        self.font = font

    def get_cell_color(self, row, column, generation, time):
        # Position of the cell relative to the center
        center = self.simulationSize / 2

        x = column * 4 + 2
        y = row * 4 + 2

        distance = math.sqrt((x - center) ** 2 + (y - center) ** 2)

        # Create a continuously changing hue
        hue = (generation * 12 + time * 40 + distance * 0.25) % 360

        # Convert HSV to RGB
        color = pygame.Color(0, 0, 0)
        color.hsva = (hue, 80, 100, 100)

        return (color.r, color.g, color.b)

    def draw_cells(self, grid, generation):
        time = pygame.time.get_ticks() / 1000

        for row in range(grid.gridSize):

            for column in range(grid.gridSize):

                if grid.get_cell(row, column) == 1:

                    x = column * grid.cellSize
                    y = row * grid.cellSize

                    color = self.get_cell_color(row, column, generation, time)

                    # Outer glow
                    glow_surface = pygame.Surface(
                        (grid.cellSize + 4, grid.cellSize + 4), pygame.SRCALPHA
                    )

                    glow_color = (color[0], color[1], color[2], 45)

                    pygame.draw.rect(
                        glow_surface,
                        glow_color,
                        (0, 0, grid.cellSize + 4, grid.cellSize + 4),
                        border_radius=2,
                    )

                    self.window.blit(glow_surface, (x - 2, y - 2))

                    # Main cell
                    pygame.draw.rect(
                        self.window,
                        color,
                        (x, y, grid.cellSize, grid.cellSize),
                        border_radius=1,
                    )

    def draw_grid(self, grid):

        for x in range(0, self.simulationSize, grid.cellSize):

            pygame.draw.line(
                self.window, (25, 25, 25), (x, 0), (x, self.simulationSize)
            )

        for y in range(0, self.simulationSize, grid.cellSize):

            pygame.draw.line(
                self.window, (25, 25, 25), (0, y), (self.simulationSize, y)
            )

    def draw_button(self, button, text):

        # Button
        pygame.draw.rect(self.window, (35, 35, 35), button, border_radius=6)

        # Border
        pygame.draw.rect(self.window, (80, 80, 80), button, 1, border_radius=6)

        button_text = self.font.render(text, True, (255, 255, 255))

        text_rect = button_text.get_rect(center=button.center)

        self.window.blit(button_text, text_rect)

    def draw_controls(self, controls, generation, simulation_running):

        # Control panel
        pygame.draw.rect(self.window, (12, 12, 12), self.controlArea)

        # Buttons
        self.draw_button(controls.startButton, "Start")

        self.draw_button(controls.stopButton, "Stop")

        self.draw_button(controls.restartButton, "Restart")

        self.draw_button(controls.stepButton, "Step")

        # Generation
        generation_text = self.font.render(
            f"Generation: {generation}", True, (220, 220, 220)
        )

        self.window.blit(generation_text, (20, 890))

        # Status
        if simulation_running:
            status = "Running"
        else:
            status = "Stopped"

        status_text = self.font.render(f"Status: {status}", True, (220, 220, 220))

        self.window.blit(status_text, (200, 890))

        # Speed title
        speed_title = self.font.render("Simulation Speed", True, (220, 220, 220))

        self.window.blit(speed_title, (550, 810))

        # Slider track
        pygame.draw.rect(self.window, (60, 60, 60), controls.slider, border_radius=5)

        # Slider handle position
        percentage = (controls.slider_max - controls.slider_value) / (
            controls.slider_max - controls.slider_min
        )

        slider_position = int(controls.slider.left + percentage * controls.slider.width)

        pygame.draw.circle(
            self.window, (220, 220, 220), (slider_position, controls.slider.centery), 8
        )

        # Speed labels
        slow_text = self.font.render("Slow", True, (150, 150, 150))

        fast_text = self.font.render("Fast", True, (150, 150, 150))

        self.window.blit(slow_text, (520, 845))

        self.window.blit(fast_text, (685, 845))

    def draw_boundary(self, simulation_area):

        pygame.draw.rect(self.window, (120, 120, 120), simulation_area, 1)
