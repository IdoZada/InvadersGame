# imports
from states.background import BackgroundState
from states.exit import ExitState
from states.interstitial import *
from states.menu import MainMenuState
from states.play_game import PlayGameState
from states.option import OptionState
from states.spaceship import SpaceShipState

"""
----------------------------------------------------------------------------------------------------
Application Entry Point
main entry point to the application. Sets up the objects and starts the main loop.
----------------------------------------------------------------------------------------------------
"""

SCREEN_W = 800
SCREEN_H = 600
invadersGame = InvadersGame("Invaders", SCREEN_W, SCREEN_H)
mainMenuState = MainMenuState(invadersGame)
gameOverState = InterstitialState(invadersGame, 'G A M E  O V E R !', 3000, mainMenuState)
exitState = ExitState(invadersGame,mainMenuState)
playGameState = PlayGameState(invadersGame, gameOverState , mainMenuState,exitState)
exitState.setGameState(playGameState)
getReadyState = InterstitialState(invadersGame, 'Get Ready!', 2000, playGameState)
mainMenuState.setPlayState(getReadyState)
optionState = OptionState(invadersGame)
getOptionState = InterstitialState(invadersGame, 'Enter To Options!', 2000, optionState)
mainMenuState.setOptionState(getOptionState)
getMainMenuState = InterstitialState(invadersGame, 'Back To Main Menu!', 2000, mainMenuState)
optionState.setMainMenuState(getMainMenuState)
backgroundState = BackgroundState(invadersGame)
getBackgroundState = InterstitialState(invadersGame, 'Go To Backgrounds!', 2000, backgroundState)
optionState.setBackgroundState(getBackgroundState)
backgroundState.setOptionState(getOptionState)
spaceShipState = SpaceShipState(invadersGame)
getSpaceShipState = InterstitialState(invadersGame, 'Go To Spaceships!', 2000, spaceShipState)
optionState.setSpaceShipState(getSpaceShipState)
spaceShipState.setOptionState(getOptionState)
invadersGame.run(mainMenuState)
