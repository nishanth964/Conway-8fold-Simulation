import pygame


class Game:
    def __init__(self):
        pygame.init()

        # Set up the game window.
        self.width = 800
        self.height = 950
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Conway: 8Fold Simulation")

        self.clock = pygame.time.Clock()

    def run(self):
        self.running = True

        while self.running:
            # Handle events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Display the current frame.
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()