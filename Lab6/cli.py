# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import *

if __name__ == '__main__':
    board = make_empty_board()
    winner = None

    player = check_first_turn(prompt_input('turn'))
    count = 0

    while winner is None and count <= 9:
        move = check_move(prompt_input('move', player), player, board)

        winner = get_winner(board)
        print_board(board, winner)

        player = switch_player(player)
        count += 1

    if winner:
        print(f"Player {player} is the winner!")
    else:
        print(f"There's no winner. Try again!")
