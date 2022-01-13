import pygame

"""
----------------------------------------------------------------------------------------------------
    PlayerView

    Renders the player tank.
----------------------------------------------------------------------------------------------------
"""


class PlayerView:

    def __init__(self, player, imgpath):
        self.player = player
        self.image = pygame.image.load(imgpath)

    def render(self, surface):
        surface.blit(self.image, (self.player.model.x, self.player.model.y, 32, 32))
