from states.Invaders_Game import *
from utils.pygamefont import *

"""
----------------------------------------------------------------------------------------------------
Background class which controls the backgrounds of all game screens.
----------------------------------------------------------------------------------------------------
"""


class BackgroundState(GameState):

    def __init__(self, game):
        super(BackgroundState, self).__init__(game)
        self.mainMenuState = None
        self.optionState = None
        self.font = FontType("Ariel", 50, (255, 255, 255))
        self.font_text = FontType("Ariel", 25, (255, 255, 255))
        self.index = 0
        self.inputTick = 0
        self.OptionItems = ['Press Enter to select your background']
        self.backgrounds = ['media/background_space.jpg', 'media/background_space_blue.png', 'media/background_space_purple.jpg', 'media/background-black.png']
        self.myBackgrounds = self.loadBackgrounds(self, self.backgrounds)
        SCREEN_W = 800
        SCREEN_H = 600
        self.surface = pygame.display.set_mode((SCREEN_W, SCREEN_H))

    def setMainMenuState(self, state):
        self.mainMenuState = state

    def setOptionState(self, state):
        self.optionState = state

    @staticmethod
    def loadBackgrounds(self, backgrounds):
        resized_backgrounds = []
        for background in backgrounds:
            pic = pygame.image.load(background)
            pic = pygame.transform.scale(pic, (400, 300))
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
                    self.index = len(self.myBackgrounds) - 1
            elif keys[K_RIGHT]:
                self.index += 1
                if self.index == len(self.myBackgrounds):
                    self.index = 0
                self.draw(self.surface)
        elif self.inputTick > 0:
            self.inputTick -= gameTime

        if self.inputTick < 0:
            self.inputTick = 0

        if keys[K_RETURN]:
            self.game.changeState(self.optionState)  # exit the game
            self.game.background = pygame.transform.scale(pygame.image.load(self.backgrounds[self.index]), (800, 600))

    def draw(self, surface):
        self.font.centre(surface, "Background", 48)
        surface.blit(self.myBackgrounds[self.index], (200, 150))
        surface.blit(pygame.transform.scale(pygame.image.load('media/right_arrow.png'), (70, 70)), (680, 250))
        surface.blit(pygame.transform.scale(pygame.image.load('media/left_arrow.png'), (70, 70)), (60, 250))
        y = surface.get_rect().height - len(self.OptionItems) * 110
        self.font_text.draw(surface, self.OptionItems[0], 250, y)
