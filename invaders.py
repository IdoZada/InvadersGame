import pygame, os, sys
from pygame.locals import *

# Our imports
from raspigame import *
from interstitial import *
from menu import MainMenuState
from invadersgame import PlayGameState
from option import OptionState

"""
----------------------------------------------------------------------------------------------------
Application Entry Point
Main entry point to the application. Sets up the objects and starts the main loop.
----------------------------------------------------------------------------------------------------
"""
SCREEN_W = 800
SCREEN_H = 600
exit = True
while exit:
    invadersGame = RaspberryPiGame("Invaders", SCREEN_W, SCREEN_H)
    mainMenuState = MainMenuState(invadersGame)
    gameOverState = InterstitialState(invadersGame, 'G A M E  O V E R !', 5000, mainMenuState)
    playGameState = PlayGameState(invadersGame, gameOverState)
    getReadyState = InterstitialState(invadersGame, 'Get Ready!', 2000, playGameState)
    mainMenuState.setPlayState(getReadyState)
    optionState = OptionState(invadersGame)
    getOptionState = InterstitialState(invadersGame, 'Enter To Options!', 2000, optionState)
    mainMenuState.setOptionState(getOptionState)
    getMainMenuState = InterstitialState(invadersGame, 'Back To Main Menu!', 2000, mainMenuState)
    optionState.setMainMenuState(getMainMenuState)
    invadersGame.run(mainMenuState)


# TODO: #### Option ######

# optionState.setMainMenuState(mainMenuState)


