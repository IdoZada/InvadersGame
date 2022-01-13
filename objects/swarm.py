# imports
from objects.bullet import *

"""
----------------------------------------------------------------------------------------------------
InvaderModel
Representation of an alien lifeform. Boiled down to its basic attributes; position on the 
playing field, its type and the current animation frame.
----------------------------------------------------------------------------------------------------
"""


class InvaderModel:
    def __init__(self, x, y, alientype):
        self.x = x
        self.y = y
        self.alientype = alientype
        self.animframe = 0

    def flipframe(self):
        if self.animframe == 0:
            self.animframe = 1
        else:
            self.animframe = 0

    def hit(self, x, y, width, height):
        return x >= self.x and y >= self.y and x + width <= self.x + 32 and y + height <= self.y + 32






