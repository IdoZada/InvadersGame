# imports
from states.play_game import *


class ExplosionModel:

    def __init__(self, x, y, maxFrames, speed, nextState=None):
        self.x = x
        self.y = y
        self.maxFrames = maxFrames
        self.speed = speed
        self.initialSpeed = speed
        self.frame = 0
        self.nextState = nextState


class ExplosionModelList:

    def __init__(self, game):
        self.explosions = []
        self.game = game

    def add(self, explosion, nextState=None):
        x, y, frames, speed = explosion
        exp = ExplosionModel(x, y, frames, speed, nextState)
        self.explosions.append(exp)

    def cleanUp(self):

        killList = []

        for e in self.explosions:
            if e.frame == e.maxFrames:
                killList.append(e)

        nextState = None

        for e in killList:
            if nextState is None and e.nextState is not None:
                nextState = e.nextState

            self.explosions.remove(e)

        if nextState is not None:
            self.game.changeState(nextState)
