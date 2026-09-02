import pygame


class Controls:

    def __init__(self):

        # Buttons
        self.startButton = pygame.Rect(20, 830, 100, 40)

        self.stopButton = pygame.Rect(140, 830, 100, 40)

        self.restartButton = pygame.Rect(260, 830, 100, 40)

        self.stepButton = pygame.Rect(380, 830, 100, 40)

        # Speed slider
        self.slider = pygame.Rect(520, 830, 200, 10)

        # Larger clickable area
        self.slider_area = pygame.Rect(510, 810, 220, 50)

        self.slider_min = 0.05
        self.slider_max = 1.0
        self.slider_value = 0.5
        self.slider_dragging = False

    def update_slider(self, x):

        x = max(self.slider.left, min(x, self.slider.right))

        percentage = (x - self.slider.left) / self.slider.width

        self.slider_value = round(
            self.slider_max - percentage * (self.slider_max - self.slider_min), 2
        )

        return self.slider_value
