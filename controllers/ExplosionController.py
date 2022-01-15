from objects.collision import ExplosionModelList


class ExplosionController:

    def __init__(self, game):
        self.list = ExplosionModelList(game)

    def update(self, gameTime):
        for e in self.list.explosions:
            e.speed -= gameTime
            if e.speed < 0:
                e.speed += e.initialSpeed
                e.frame += 1

        self.list.cleanUp()
