# imports
import pygame, os, sys
from pygame.locals import *

"""
----------------------------------------------------------------------------------------------------
BulletView

Renders the bullets for the player's missiles.
----------------------------------------------------------------------------------------------------
"""


class BulletView:

    def __init__(self, bulletController, imgpath):
        self.BulletController = bulletController
        self.image = pygame.image.load(imgpath)

    def render(self, surface):
        for b in self.BulletController.bullets:
            surface.blit(self.image, (b.x, b.y, 8, 8))
