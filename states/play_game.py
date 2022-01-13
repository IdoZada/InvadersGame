import constants.const as const

# controllers
from controllers.CollisionController import CollisionController
from controllers.ExplosionController import ExplosionController
from controllers.PlayerController import PlayerController
from controllers.SwarmController import SwarmController

# objects
from objects.collision import *
from objects.swarm import *

# views
from views.BulletView import BulletView
from views.ExplosionView import ExplosionView
from views.InvaderView import InvaderView

# states
from states.Invaders_Game import GameState
from states.interstitial import InterstitialState
from views.PlayerLivesView import PlayerLivesView
from views.PlayerView import PlayerView

from utils.font import *
import pygame
from pygame.locals import *


class PlayGameState(GameState):

    def __init__(self, game, gameOverState,  mainMenuState, exitGameState):
        super(PlayGameState, self).__init__(game)
        self.controllers = None
        self.renderers = None
        self.player_controller = None
        self.swarm_controller = None
        self.swarmSpeed = 500
        self.gameOverState = gameOverState
        self.mainMenuState = mainMenuState
        self.exitGameState = exitGameState
        self.exitMessage = FontType("Ariel", 50, (255, 255, 255))
        self.initialise()

    def onEnter(self, previousState):
        self.player_controller.pause(False)

    def initialise(self):
        self.swarm_controller = SwarmController(800, 48, self.swarmSpeed)
        swarm_renderer = InvaderView(self.swarm_controller, '../media/monsters_anim.png')

        self.player_controller = PlayerController(0, 540)
        player_renderer = PlayerView(self.player_controller, self.game.spaceship)
        lives_renderer = PlayerLivesView(self.player_controller, self.game.spaceship)
        bullet_renderer = BulletView(self.player_controller.bullets, '../media/bullet.png')
        alienbullet_renderer = BulletView(self.swarm_controller.bullets, "../media/alienbullet.png")

        explosion_controller = ExplosionController(self.game)
        collision_controller = CollisionController(self.game, self.swarm_controller, self.player_controller
                                                   , explosion_controller, self)

        explosion_view = ExplosionView(explosion_controller.list.explosions, '../media/explosion.png', 32, 32)

        self.renderers = [alienbullet_renderer, swarm_renderer, bullet_renderer, player_renderer, lives_renderer,
                          explosion_view]
        self.controllers = [self.swarm_controller, self.player_controller, collision_controller, explosion_controller]

    def update(self, gameTime):
        self.renderers[3] = PlayerView(self.player_controller, self.game.spaceship)
        self.renderers[4] = PlayerLivesView(self.player_controller, self.game.spaceship)

        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            self.game.changeState(self.exitGameState)

        for ctrl in self.controllers:
            ctrl.update(gameTime)

        if self.player_controller.model.lives == 0:
            self.game.changeState(self.gameOverState)
            self.initialise()

        if len(self.swarm_controller.invaders) == 0:
            self.swarmSpeed -= 50
            if self.swarmSpeed < 100:
                self.swarmSpeed = 100

            self.swarm_controller.reset(48, self.swarmSpeed)
            levelUpMessage = InterstitialState(self.game, const.CONGRATULATIONS_LEVEL_UP, 2000, self)
            self.game.changeState(levelUpMessage)
            self.player_controller.model.level += 1

    def draw(self, surface):
        for view in self.renderers:
            view.render(surface)
