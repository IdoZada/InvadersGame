import pygame, os, sys
from pygame.locals import *

# Our imports
from background import BackgroundState
from interstitial import *
from menu import MainMenuState
from invadersgame import PlayGameState
from option import OptionState
from spaceship import SpaceShipState

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
optionState = OptionState(invadersGame)
getOptionState = InterstitialState(invadersGame, 'Enter To Options!', 2000, optionState)
mainMenuState.setOptionState(getOptionState)
getMainMenuState = InterstitialState(invadersGame, 'Back To Main Menu!', 2000, mainMenuState)
optionState.setMainMenuState(getMainMenuState)
backgroundState = BackgroundState(invadersGame)
getBackgroundState = InterstitialState(invadersGame, 'Go to Background!', 2000, backgroundState)
optionState.setBackgroundState(getBackgroundState)
backgroundState.setOptionState(getOptionState)
spaceShipState = SpaceShipState(invadersGame)
getSpaceShipState = InterstitialState(invadersGame, 'Go to Spaceship!', 2000, spaceShipState)
optionState.setSpaceShipState(getSpaceShipState)
spaceShipState.setOptionState(getOptionState)
invadersGame.run(mainMenuState)


