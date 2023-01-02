# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import *

if __name__ == '__main__':

    while True:

        # welcomes the user and prompts game mode
        prompt_mode = (f"Welcome to the Tic Tac Toe!\n"
                       f"Select the mode to start gaming:\n"
                       f"\t1 for a battle with the computer;\n"
                       f"\t2 for a double with your friend.\n"
                       f"\t3 for an automated cyber battle.\n"
                       f"\tAnything else to check global stats.\n")
        mode = input(prompt_mode)

        while not mode.isdigit() and mode not in range(1, 4):
            # sanity checks the game mode
            mode = input("Pick a valid number between 1 and 3!\n")

        if int(mode) == 1:
            # prompts the user to pick a turn
            turn = input("Pick a turn for you, X or O? X goes first.\n")
            while turn not in ['X', 'O', 'x', 'o']:
                turn = input("Pick a valid symbol between X and O!\n")

            if turn.upper() == 'X':
                # user chooses to go first
                player_1 = Human('X')
                player_2 = Bot('O')
            else:
                # user chooses to go last
                player_1 = Bot('X')
                player_2 = Human('O')

        elif int(mode) == 2:
            # initiates two human instances for double players
            player_1 = Human('X')
            player_2 = Human('O')
        elif int(mode) == 3:
            # initiates two bot instances for fun
            player_1 = Bot('X')
            player_2 = Bot('O')
        else:
            stats = Stats()
            stats.winner_ratio()
            stats.bot_order()
            stats.human_vs_bot()
            break

        # initiates the game with two players
        game = Game(player_1, player_2)
        game.play_game()

        if game.resume:
            break
