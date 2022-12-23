# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.

import random
import numpy as np
from itertools import cycle
# from typing import NamedTuple


class Game:
    def __init__ (self, player_1, player_2):
        """Initializes a game with default settings"""

        # sets players as in selected mode
        self._player_1, self._player_2 = player_1, player_2
        self._players = (self._player_1, self._player_2)
        self.players = cycle(self._players)
        self.player = next(self.players)

        # sets clear board and winner info
        self.board = None
        self.make_empty_board()
        self.winner = None
        self.count = 0

    def make_empty_board (self):
        """Initializes an empty board to start the game."""

        self.board = np.empty((3, 3), object)

    def print_board (self):
        """Prints the current status of the board and total scores."""

        # convert the board for better display
        # no need for modification if data structure saves 0 rather than None
        mod_board = [col if col else " " for row in self.board for col in row]

        print(f"Tic-tac-toe Scoreboard\n\n"
              f"\t  {mod_board[0]} | {mod_board[1]} | {mod_board[2]}  \n"
              f"\t ———|———|——— \t\n"
              f"\t  {mod_board[3]} | {mod_board[4]} | {mod_board[5]}  \n"
              f"\t ———|———|——— \t\n"
              f"\t  {mod_board[6]} | {mod_board[7]} | {mod_board[8]}  \n"
              f"\nCurrent winner: {self.winner}")

    def get_winner (self):
        """Determines the winner of the given board.
        Returns 'X', 'O', or None."""

        # convert text strings to int values for easier calculation and comparison
        mod_board = [[-1 if ele == 'O' else 1 if ele == 'X' else 0 for ele in row]
                     for row in self.board]

        # sums of values in rows and columns of the board
        rows = [sum(i) for i in mod_board]
        columns = [sum(i) for i in zip(*mod_board)]

        # convert diagonal values to lists
        dec_diagonal = [mod_board[i][i] for i in range(len(mod_board))]
        inc_diagonal = [mod_board[i][len(mod_board) - 1 - i] for i in range(len(mod_board))]

        # concatenate sums of eight routes in a list for final check
        sum_temp = rows + columns + [sum(dec_diagonal)] + [sum(inc_diagonal)]

        # conditional result return based on the sum of each route
        return 'O' if -3 in sum_temp else 'X' if 3 in sum_temp else None

    def switch_player (self):
        """Toggle between two players."""

        self.player = next(self.players)

    def update_board(self, row, column, player):
        """Updates the board to reflect the move a player makes."""

        self.board[row][column] = player

    def reset_game (self):
        """Resets the game to its initial state."""

        self.board = None
        self.make_empty_board()
        self.winner = None

    def play_game (self):
        """Runs the main body of the game after mode selection."""

        while not self.winner and self.count <= 9:
            self.player.get_move(self.board)
            self.winner = self.get_winner() if self.count >= 5 else None
            self.print_board()
            self.switch_player()
            self.count += 1

        if self.winner:
            print(f"Player {self.player} is the winner!")
        else:
            print(f"There's no winner. Try again!")


class Human:
    def __init__ (self, player):
        """Initializes a human player that inputs moves."""

        self._player = player

    def get_move (self, board):
        """Prompts the user to make the next move.
        Validates it and updates it to the board."""

        move = input(f"Make your move, fellow player.\n")

        if not move.isdigit() or move not in range(1, 10):
            # check if the input is the correct type
            print("Please make your move as a numerical number in the range 1-9.")
            return self.get_move(board)
        else:
            move = int(move)

        # conversion from integer to 2d location
        row = int((move - 1) / 3)
        column = int((move - 1) % 3)

        if board[row][column] is not None:
            # check if the move is on an available place of the board
            print("Please make your move in an available place.")
            return self.get_move(board)

        # updates move to the board in Game class through an instance
        board.update_board(row, column, self._player)


class Bot:
    def __init__ (self, player):
        """Initializes a bot player that takes random moves."""

        self._player = player

    def get_move (self, board):
        """Chooses a random spot to move from available candidates."""

        # algorithm for the bot to pick a random move from available spots
        avail = [(row, col) for row in board for col in row if not board[row][col]]
        selection = random.choice(avail)

        # updates move to the board in Game class through an instance
        board.update_board(selection[0], selection[1], self._player)


# def pick_turn (self):
#     """Sanity checks the input of the first turn."""
#
#     turn = input(f"Choose the player, X or O?\n")
#
#     if not turn.isalpha() or turn not in ['X', 'O']:
#         # check if the input is the correct type and letter
#         print("Pick a valid letter between X and O.")
#
#     return turn
