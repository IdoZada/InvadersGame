from raspigame import *
from pygamefont import *


class SpaceShipState(GameState):

    def __init__(self, game):
        super(SpaceShipState, self).__init__(game)
        self.mainMenuState = None
        self.optionState = None
        self.font = FontType("david", 50, (255, 255, 255))
        self.index = 0
        self.inputTick = 0
        self.OptionItems = []
        self.spaceships = ['ship1.png', 'ship2.png', 'ship3.png', 'ship4.png', 'ship5.png', 'ship6.png']
        self.mySpaceships = self.loadSpaceships(self.spaceships)
        SCREEN_W = 800
        SCREEN_H = 600
        self.surface = pygame.display.set_mode((SCREEN_W, SCREEN_H))


    def setMainMenuState(self, state):
        self.mainMenuState = state

    def setOptionState(self, state):
        self.optionState = state

    def loadSpaceships(self, spaceships):
        resized_backgrounds = []
        for spaceship in spaceships:
            pic = pygame.image.load(spaceship)
            pic = pygame.transform.scale(pic, (100,100))
            resized_backgrounds.append(pic)
        return resized_backgrounds

    def update(self, gameTime):
        keys = pygame.key.get_pressed()
        if (keys[K_LEFT] or keys[K_RIGHT]) and self.inputTick == 0:
            self.inputTick = 250
            if keys[K_LEFT]:
                self.index -= 1
                self.draw(self.surface)
                if self.index < 0:
                    self.index = len(self.mySpaceships) - 1
            elif keys[K_RIGHT]:
                self.index += 1
                if self.index == len(self.mySpaceships):
                    self.index = 0
                self.draw(self.surface)
        elif self.inputTick > 0:
            self.inputTick -= gameTime

        if self.inputTick < 0:
            self.inputTick = 0

        if keys[K_RETURN]:
            self.game.changeState(self.optionState)  # go to option state
            # print(self.spaceships[self.index])
            self.game.spaceship = self.spaceships[self.index]

    def draw(self, surface):
        self.font.centre(surface, "Spaceship", 48)
        surface.blit(self.mySpaceships[self.index], (350, 250))
        surface.blit(pygame.transform.scale(pygame.image.load('right_arrow.png'), (70, 70)), (680, 250))
        surface.blit(pygame.transform.scale(pygame.image.load('left_arrow.png'), (70, 70)), (60, 250))

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
