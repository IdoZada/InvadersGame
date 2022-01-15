from utils.font import *
import pygame


"""
----------------------------------------------------------------------------------------------------
    PlayerLivesView

    Renders the number of lives left for the player.
----------------------------------------------------------------------------------------------------
"""


class PlayerLivesView:
    def __init__(self, player, imgpath):
        self.player = player
        self.image = pygame.image.load(imgpath)
        self.font = FontType("david", 25, (255, 255, 255))

    def render(self, surface):
        x = 8

        for life in range(0, self.player.model.lives):
            surface.blit(self.image, (x, 8, 32, 32))
            x += 40

        self.font.center(surface, 'Score:' + ' ' + str(self.player.model.score), 10)
        self.font.draw(surface, 'Level:' + ' ' + str(self.player.model.level), 700, 10)
