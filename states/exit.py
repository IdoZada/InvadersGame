import pygame

from states.Invaders_Game import GameState
from states.interstitial import InterstitialState
from utils.font import FontType


class ExitState(GameState):

    def __init__(self, game, mainMenuState):
        super(ExitState, self).__init__(game)
        self.mainMenuState = mainMenuState
        self.gameState = None
        self.font = FontType("Ariel", 50, (255, 255, 255))
        self.fontTitle = FontType("Ariel", 50, (255, 255, 255))
        self.index = 0
        self.inputTick = 0
        self.menuItems = ['Yes', 'No']

    def setGameState(self, state):
        self.gameState = state

    def update(self, gameTime):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_UP] or keys[pygame.K_DOWN]) and self.inputTick == 0:
            self.inputTick = 250
            if keys[pygame.K_UP]:
                self.index -= 1
                if self.index < 0:
                    self.index = len(self.menuItems) - 1
            elif keys[pygame.K_DOWN]:
                self.index += 1
                if self.index == len(self.menuItems):
                    self.index = 0
        elif self.inputTick > 0:
            self.inputTick -= gameTime

        if self.inputTick < 0:
            self.inputTick = 0

        if keys[pygame.K_RETURN]:
            if self.index == 0:
                exitFromGame = InterstitialState(self.game, 'Exit From GAME', 2000, self.mainMenuState)
                self.game.changeState(exitFromGame)
                self.gameState.initialise()
            elif self.index == 1:
                self.game.changeState(self.gameState)

    def draw(self, surface):
        self.fontTitle.center(surface, "Are you sure to exit from the game?", 100)
        count = 0
        y = surface.get_rect().height - len(self.menuItems) * 150
        for item in self.menuItems:
            itemText = "  "

            if count == self.index:
                itemText = "> "

            itemText += item
            self.font.draw(surface, itemText, 350, y)
            y += 50
            count += 1