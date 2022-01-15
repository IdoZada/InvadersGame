
# controllers
from controllers.BulletController import BulletController
# objects
from objects.swarm import InvaderModel

"""
----------------------------------------------------------------------------------------------------
Swarm
The swarm updates all the alien invaders. It handles movement and collision detection.
----------------------------------------------------------------------------------------------------
"""


class SwarmController:

    def __init__(self, scrwidth, offsety, initialframeticks):

        self.currentframecount = initialframeticks
        self.framecount = initialframeticks
        self.invaders = []
        self.sx = -8
        self.move_down = False
        self.alienslanded = False
        self.bullets = BulletController(200)  # pixels per sec
        self.alienShooter = 3  # each 3rd alien (to start with) fires
        self.bulletDropTime = 2500
        self.shootTimer = self.bulletDropTime  # each bullet is fired in this ms interval
        self.currentShooter = 0  # current shooting alien
        self.collision = False
        self.positionInvaders(offsety) # Position the invaders in the swarm

    def reset(self, offsety, ticks):
        self.currentframecount = ticks
        self.framecount = ticks

        self.positionInvaders(offsety)

    def positionInvaders(self, offsety):
        for y in range(7):
            for x in range(10):
                invader = InvaderModel(160 + (x * 48) + 8, (y * 32) + offsety, y % 2)
                self.invaders.append(invader)

    def update(self, gameTime):

        self.bullets.update(gameTime)
        self.framecount -= gameTime
        movesideways = True

        if self.framecount < 0:
            if self.move_down:
                self.move_down = False
                movesideways = False
                self.sx *= -1
                self.bulletDropTime -= 250
                if self.bulletDropTime < 1000:
                    self.bulletDropTime = 1000
                self.currentframecount -= 100
                if self.currentframecount < 200:  # clamp the speed of the aliens to 200ms
                    self.currentframecount = 200

                for i in self.invaders:
                    i.y += 32

            self.framecount = self.currentframecount + self.framecount
            for i in self.invaders:
                i.flipframe()

            if movesideways:
                for i in self.invaders:
                    i.x += self.sx

            x, y, width, height = self.getarea()

            if x <= 0 and self.sx < 0 or x + width >= 800 and self.sx > 0:
                if y + height >= 500:
                    self.collision = True
                self.move_down = True

        self.shootTimer -= gameTime
        if self.shootTimer <= 0:
            self.shootTimer += self.bulletDropTime  # reset the timer
            self.currentShooter += self.alienShooter

            self.currentShooter = self.currentShooter % len(self.invaders)

            shooter = self.invaders[self.currentShooter]
            x = shooter.x + 9  # bullet is 8 pixels
            y = shooter.y + 16
            self.bullets.addBullet(x, y)

    def getarea(self):
        leftmost = 2000
        rightmost = -2000
        topmost = -2000
        bottommost = 2000

        for i in self.invaders:
            if i.x < leftmost:
                leftmost = i.x

            if i.x > rightmost:
                rightmost = i.x

            if i.y < bottommost:
                bottommost = i.y

            if i.y > topmost:
                topmost = i.y

        width = (rightmost - leftmost) + 32
        height = (topmost - bottommost) + 32

        return leftmost, bottommost, width, height
