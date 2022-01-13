import pygame
from pygame.locals import *

# controllers
from controllers.BulletController import BulletController
from objects.player import PlayerModel

"""
----------------------------------------------------------------------------------------------------
    Player

    The tank at the bottom of the screen.
----------------------------------------------------------------------------------------------------
"""


class PlayerController:
    def __init__(self, x, y):
        self.model = PlayerModel(x, y)
        self.isPaused = False
        self.bullets = BulletController(-200)  # pixels per sec
        self.shootSound = pygame.mixer.Sound('../media/playershoot.wav')

    def pause(self, isPaused):
        self.isPaused = isPaused

    def update(self, gameTime):

        self.bullets.update(gameTime)

        if self.isPaused:
            return

        keys = pygame.key.get_pressed()

        if keys[K_RIGHT] and self.model.x < 800 - 32:
            self.model.x += (gameTime / 1000.0) * self.model.speed
        elif keys[K_LEFT] and self.model.x > 0:
            self.model.x -= (gameTime / 1000.0) * self.model.speed

        if keys[K_SPACE] and self.bullets.canFire():
            x = self.model.x + 9  # bullet is 8 pixels
            y = self.model.y - 16
            self.bullets.addBullet(x, y)
            self.shootSound.play()

    def hit(self, x, y, width, height):
        return x >= self.model.x and y >= self.model.y and x + width <= self.model.x + 32 and y + height <= self.model.y + 32
