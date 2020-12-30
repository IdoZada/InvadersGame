from states.Invaders_Game import *
from utils.font import *


class OptionState(GameState):

    def __init__(self, game):
        super(OptionState, self).__init__(game)
        self.mainMenuState = None
        self.backgroundState = None
        self.spaceShipState = None
        self.OptionItems = ['Background', 'Spaceship', 'Back']
        self.font = FontType("Ariel", 50, (255, 255, 255))
        self.index = 0
        self.inputTick = 0

    """
       Initialize the instance of state to move.
    """
    def setMainMenuState(self, state):
        self.mainMenuState = state

    """
        Initialize the instance of state to move.
    """
    def setBackgroundState(self, state):
        self.backgroundState = state

    """
        Initialize the instance of state to move.
    """
    def setSpaceShipState(self, state):
        self.spaceShipState = state

    def update(self, gameTime):

        keys = pygame.key.get_pressed()
        if (keys[K_UP] or keys[K_DOWN]) and self.inputTick == 0:
            self.inputTick = 250
            if keys[K_UP]:
                self.index -= 1
                if self.index < 0:
                    self.index = len(self.OptionItems) - 1
            elif keys[K_DOWN]:
                self.index += 1
                if self.index == len(self.OptionItems):
                    self.index = 0
        elif self.inputTick > 0:
            self.inputTick -= gameTime

        if self.inputTick < 0:
            self.inputTick = 0

        if keys[K_RETURN]:
            if self.index == 2:
                self.game.changeState(self.mainMenuState)  # back to main menu
            elif self.index == 0:
                self.game.changeState(self.backgroundState)  # go to background state
            elif self.index == 1:
                self.game.changeState(self.spaceShipState)  # go to spaceship state

    def draw(self, surface):

        self.font.center(surface, "Options", 48)

        count = 0
        y = surface.get_rect().height - len(self.OptionItems) * 110
        for item in self.OptionItems:
            itemText = "  "

            if count == self.index:
                itemText = "> "

            itemText += item
            self.font.draw(surface, itemText, 300, y)
            y += 50
            count += 1