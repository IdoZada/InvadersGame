# imports
import pygame, os, sys
from pygame.locals import *

"""
----------------------------------------------------------------------------------------------------
    InvaderView

    Draws each invader in their position on the playing field with the correct frame.
----------------------------------------------------------------------------------------------------
"""


class InvaderView:

    def __init__(self, swarm, imgpath):
        self.image = pygame.image.load(imgpath)
        self.swarm = swarm

    def render(self, surface):
        for i in self.swarm.invaders:
            surface.blit(self.image, (i.x, i.y, 32, 32), (i.animframe * 32, 32 * i.alientype, 32, 32))
