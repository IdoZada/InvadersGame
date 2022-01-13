
# imports
from states.interstitial import *


class CollisionController:

    def __init__(self, game, swarm, player, explosionController, playState):
        self.swarm = swarm
        self.player = player
        self.game = game
        self.BulletController = player.bullets
        self.EnemyBullets = swarm.bullets
        self.expCtrl = explosionController
        self.playGameState = playState
        self.alienDeadSound = pygame.mixer.Sound('../media/aliendie.wav')
        self.playerDie = pygame.mixer.Sound('../media/playerdie.wav')

    def update(self, gameTime):

        aliens = []
        bullets = []

        for b in self.BulletController.bullets:

            if bullets.count(b) > 0:
                continue

            for inv in self.swarm.invaders:
                if inv.hit(b.x + 3, b.y + 3, 8, 12):
                    aliens.append(inv)
                    bullets.append(b)
                    break

        for b in bullets:
            self.BulletController.removeBullet(b)

        for inv in aliens:
            self.swarm.invaders.remove(inv)
            self.player.model.score += (10 * (inv.alientype + 1))
            self.expCtrl.list.add((inv.x, inv.y, 6, 50))
            self.alienDeadSound.play()

        playerHit = False

        for b in self.EnemyBullets.bullets:
            if self.player.hit(b.x + 3, b.y + 3, 8, 12):
                self.player.model.lives -= 1
                playerHit = True
                break

        if self.swarm.collision:
            self.playerDie.play()
            self.playGameState.initialise()
            tryAgainMessage = InterstitialState(self.game, 'Try Again!', 2000, self.playGameState)
            self.game.changeState(tryAgainMessage)

        if playerHit:
            self.EnemyBullets.clear()
            self.player.bullets.clear()

            if self.player.model.lives > 0:
                self.player.pause(True)
                getReadyState = InterstitialState(self.game, 'Get Ready!', 2000, self.playGameState)
                self.expCtrl.list.add((self.player.model.x, self.player.model.y, 6, 50), getReadyState)

            self.playerDie.play()
