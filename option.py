from raspigame import *
from pygamefont import *


#TODO: Connect to the mainmenu, buttons
class OptionState(GameState):

    def __init__(self, game):
        super(OptionState, self).__init__(game)
        self.mainMenuState = None
        self.font = FontType("david", 50, (255, 255, 255))
        self.index = 0
        self.inputTick = 0
        self.OptionItems = ['Default', 'Ok']

    def setMainMenuState(self, state):
        self.mainMenuState = state

    def update(self, gameTime):

        keys = pygame.key.get_pressed()
        if ((keys[K_UP] or keys[K_DOWN]) and self.inputTick == 0):
            self.inputTick = 250
            if (keys[K_UP]):
                self.index -= 1
                if (self.index < 0):
                    self.index = len(self.OptionItems) - 1
            elif (keys[K_DOWN]):
                self.index += 1
                if (self.index == len(self.OptionItems)):
                    self.index = 0
        elif (self.inputTick > 0):
            self.inputTick -= gameTime

        if (self.inputTick < 0):
            self.inputTick = 0

        if (keys[K_RETURN]):
            if (self.index == 1):
                print(self.mainMenuState)
                self.game.changeState(self.mainMenuState)  # exit the game
            elif (self.index == 0):
                print(self.playGameState)
                self.game.changeState(self.playGameState)

    def draw(self, surface):

        self.font.centre(surface, "Options", 48)

        count = 0
        y = surface.get_rect().height - len(self.OptionItems) * 110
        for item in self.OptionItems:
            itemText = "  "

            if (count == self.index):
                itemText = "> "

            itemText += item
            self.font.draw(surface, itemText, 300, y)
            y += 50
            count += 1