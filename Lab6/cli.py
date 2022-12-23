# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import *

if __name__ == '__main__':

    # welcomes the user and prompts game mode
    prompt_mode = (f"Welcome to the Tic Tac Toe!\n"
                   f"Select the mode to start gaming:\n"
                   f"1 for a battle with the computer and 2 for a double with your friend.\n")
    mode = input(prompt_mode)

    while not mode.isdigit() and mode not in range(1, 3):
        # sanity checks the game mode
        mode = input(f"Pick a valid number between 1 and 2!")

    if int(mode) == 1:
        # initiates a human instance and a bot instance for single player
        player_1 = Human('X')
        player_2 = Bot('O')
    else:
        # initiates two human instances for double players
        player_1 = Human('X')
        player_2 = Human('O')

    game = Game(player_1, player_2)
    game.play_game()