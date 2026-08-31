import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.WIDTH = 800
        self.HEIGHT = 950
        self.WINDOW = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Conway: 8Fold Simulation") 
        self.clock = pygame.time.Clock()

    def run(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()