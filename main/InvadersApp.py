# imports
import constants.const as const

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


invadersGame = InvadersGame(const.GAME_NAME, const.SCREEN_W, const.SCREEN_H)
mainMenuState = MainMenuState(invadersGame)
gameOverState = InterstitialState(invadersGame, const.GAME_OVER, 3000, mainMenuState)
exitState = ExitState(invadersGame, mainMenuState)
playGameState = PlayGameState(invadersGame, gameOverState, mainMenuState, exitState)
exitState.setGameState(playGameState)
getReadyState = InterstitialState(invadersGame, const.GET_READY, 2000, playGameState)
mainMenuState.setPlayState(getReadyState)
optionState = OptionState(invadersGame)
getOptionState = InterstitialState(invadersGame, const.ENTER_THE_OPTION, 2000, optionState)
mainMenuState.setOptionState(getOptionState)
getMainMenuState = InterstitialState(invadersGame, const.BACK_TO_MAIN_MENU, 2000, mainMenuState)
optionState.setMainMenuState(getMainMenuState)
backgroundState = BackgroundState(invadersGame)
getBackgroundState = InterstitialState(invadersGame, const.GO_TO_BACKGROUNDS, 2000, backgroundState)
optionState.setBackgroundState(getBackgroundState)
backgroundState.setOptionState(getOptionState)
spaceShipState = SpaceShipState(invadersGame)
getSpaceShipState = InterstitialState(invadersGame, const.GO_TO_SPACESHIPS, 2000, spaceShipState)
optionState.setSpaceShipState(getSpaceShipState)
spaceShipState.setOptionState(getOptionState)
invadersGame.run(mainMenuState)
