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

invadersGame = RaspberryPiGame("Invaders", SCREEN_W, SCREEN_H)
mainMenuState = MainMenuState(invadersGame)
gameOverState = InterstitialState(invadersGame, 'G A M E  O V E R !', 5000, mainMenuState)
playGameState = PlayGameState(invadersGame, gameOverState)
getReadyState = InterstitialState(invadersGame, 'Get Ready!', 2000, playGameState)
mainMenuState.setPlayState(getReadyState)
invadersGame.run(mainMenuState)

# TODO: #### Option ######
optionState = OptionState(invadersGame)
getOptionState = InterstitialState(invadersGame, 'Get Option!', 2000, optionState)
mainMenuState.setOptionState(getOptionState)
# optionState.setMainMenuState(mainMenuState)


