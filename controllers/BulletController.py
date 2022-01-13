# imports
from objects.bullet import BulletModel


"""
----------------------------------------------------------------------------------------------------
Bullet Controller

Manages the update for each bullet.
----------------------------------------------------------------------------------------------------
"""


class BulletController:

    def __init__(self, speed):
        self.countdown = 0
        self.bullets = []
        self.speed = speed

    def clear(self):
        self.bullets[:] = []

    def canFire(self):
        return self.countdown == 0 and len(self.bullets) < 3

    def addBullet(self, x, y):
        self.bullets.append(BulletModel(x, y))
        self.countdown = 1000

    def removeBullet(self, bullet):
        self.bullets.remove(bullet)

    def update(self, gameTime):

        killList = []

        if self.countdown > 0:
            self.countdown = self.countdown - gameTime
        else:
            self.countdown = 0

        for b in self.bullets:
            b.update(self.speed * (gameTime / 1000.0))
            if b.y < 0:
                killList.append(b)

        for b in killList:
            self.removeBullet(b)
