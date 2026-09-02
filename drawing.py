import math

import pygame


class Drawing:

    def __init__(self, window, simulation_size, control_area, font):

        self.window = window
        self.simulationSize = simulation_size
        self.controlArea = control_area
        self.font = font

        # Additional fonts
        self.small_font = pygame.font.Font(None, 20)

        self.tiny_font = pygame.font.Font(None, 18)

        # Reusable glow surface
        self.glow_layer = pygame.Surface(self.window.get_size(), pygame.SRCALPHA)

    def get_cell_color(self, row, column, generation, time):

        center = self.simulationSize / 2

        cell_size = 4

        x = column * cell_size + cell_size / 2

        y = row * cell_size + cell_size / 2

        distance = math.sqrt((x - center) ** 2 + (y - center) ** 2)

        hue = (generation * 12 + time * 40 + distance * 0.25) % 360

        color = pygame.Color(0, 0, 0)

        color.hsva = (hue, 80, 100, 100)

        return (color.r, color.g, color.b)

    def draw_cells(self, grid, generation):

        time = pygame.time.get_ticks() / 1000

        # Clear reusable glow layer
        self.glow_layer.fill((0, 0, 0, 0))

        live_cells = []

        for row in range(grid.gridSize):

            for column in range(grid.gridSize):

                if grid.get_cell(row, column) != 1:

                    continue

                x = column * grid.cellSize

                y = row * grid.cellSize

                color = self.get_cell_color(row, column, generation, time)

                live_cells.append((x, y, color))

                # Glow
                pygame.draw.rect(
                    self.glow_layer,
                    (color[0], color[1], color[2], 35),
                    (x - 2, y - 2, grid.cellSize + 4, grid.cellSize + 4),
                    border_radius=2,
                )

        # Draw glow first
        self.window.blit(self.glow_layer, (0, 0))

        # Draw cells over glow
        for x, y, color in live_cells:

            pygame.draw.rect(
                self.window,
                color,
                (x, y, grid.cellSize, grid.cellSize),
                border_radius=1,
            )

    def draw_grid(self, grid):

        grid_color = (22, 22, 25)

        for x in range(0, self.simulationSize, grid.cellSize):

            pygame.draw.line(self.window, grid_color, (x, 0), (x, self.simulationSize))

        for y in range(0, self.simulationSize, grid.cellSize):

            pygame.draw.line(self.window, grid_color, (0, y), (self.simulationSize, y))

    def draw_button(self, button, text):

        mouse_position = pygame.mouse.get_pos()

        hovered = button.collidepoint(mouse_position)

        if hovered:

            background = (55, 55, 60)

            border = (120, 120, 130)

        else:

            background = (30, 30, 34)

            border = (70, 70, 75)

        pygame.draw.rect(self.window, background, button, border_radius=7)

        pygame.draw.rect(self.window, border, button, 1, border_radius=7)

        button_text = self.small_font.render(text, True, (235, 235, 240))

        text_rect = button_text.get_rect(center=button.center)

        self.window.blit(button_text, text_rect)

    def draw_controls(self, controls, generation, simulation_running):

        # Control panel
        pygame.draw.rect(self.window, (12, 12, 15), self.controlArea)

        # Separator
        pygame.draw.line(
            self.window,
            (55, 55, 60),
            (0, self.simulationSize),
            (self.window.get_width(), self.simulationSize),
        )

        # Buttons
        self.draw_button(controls.startButton, "Start")

        self.draw_button(controls.stopButton, "Stop")

        self.draw_button(controls.restartButton, "Restart")

        self.draw_button(controls.stepButton, "Step")

        # Generation
        generation_text = self.small_font.render(
            f"Generation: {generation}", True, (220, 220, 225)
        )

        self.window.blit(generation_text, (20, 890))

        # Status
        if simulation_running:

            status = "Running"

        else:

            status = "Stopped"

        status_text = self.small_font.render(f"Status: {status}", True, (220, 220, 225))

        self.window.blit(status_text, (200, 890))

        # Speed title
        speed_title = self.small_font.render("Simulation Speed", True, (220, 220, 225))

        self.window.blit(speed_title, (550, 805))

        # Slider track
        pygame.draw.rect(self.window, (50, 50, 55), controls.slider, border_radius=5)

        # Slider position
        percentage = (controls.slider_max - controls.slider_value) / (
            controls.slider_max - controls.slider_min
        )

        slider_position = int(controls.slider.left + percentage * controls.slider.width)

        # Slider handle
        pygame.draw.circle(
            self.window, (225, 225, 230), (slider_position, controls.slider.centery), 8
        )

        # Slider labels
        slow_text = self.tiny_font.render("Slow", True, (145, 145, 150))

        fast_text = self.tiny_font.render("Fast", True, (145, 145, 150))

        self.window.blit(slow_text, (520, 845))

        self.window.blit(fast_text, (685, 845))

    def draw_boundary(self, simulation_area):

        pygame.draw.rect(self.window, (100, 100, 105), simulation_area, 1)
