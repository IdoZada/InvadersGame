from states.play_game import *


class ExplosionView:

    def __init__(self, explosions, explosionImg, width, height):
        self.image = pygame.image.load(explosionImg)
        self.image.set_colorkey((255, 0, 255))
        self.explosions = explosions
        self.width = width
        self.height = height

    def render(self, surface):
        for e in self.explosions:
            surface.blit(self.image, (e.x, e.y, self.width, self.height),
                         (e.frame * self.width, 0, self.width, self.height))