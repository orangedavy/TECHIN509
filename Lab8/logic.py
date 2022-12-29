# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.

import random
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from itertools import cycle, chain


class Game:
    def __init__ (self, player_1, player_2):
        """Initializes a game with default settings"""

        # sets players as in selected mode
        self.player_1, self.player_2 = player_1, player_2
        self.players = cycle((self.player_1, self.player_2))
        self.player = next(self.players)

        # sets clear board and winner info
        self.board = None
        self.make_board()
        self.winner = None
        self.count = 0
        self.resume = False
        self.stats = Stats()

    def make_board (self):
        """Initializes an empty board to start the game."""

        # self.board = np.empty((3, 3), object)
        self.board = np.zeros((3, 3), str)

    def print_board (self):
        """Prints the current board and result."""

        print(f"\nTic-tac-toe Scoreboard\n\n"
              f"\t  {self.board[0][0] or ' '} | {self.board[0][1] or ' '} | {self.board[0][2] or ' '}  \n"
              f"\t ———|———|——— \t\n"
              f"\t  {self.board[1][0] or ' '} | {self.board[1][1] or ' '} | {self.board[1][2] or ' '}  \n"
              f"\t ———|———|——— \t\n"
              f"\t  {self.board[2][0] or ' '} | {self.board[2][1] or ' '} | {self.board[2][2] or ' '}  \n"
              f"\nCurrent winner: {self.player.name}\n")

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

    def update_board (self, row, column):
        """Updates the board to reflect the move a player makes."""

        self.board[row][column] = self.player.symbol

    def play_game (self):
        """Runs the main body of the game after mode selection."""

        # game continues without a winner or a tie
        while not self.winner and self.count < 9:
            # prompts move from player and updates to board
            row, column = self.player.get_move(self.board)
            self.update_board(row, column)

            # check winner after five total moves and prints scoreboard
            self.winner = self.get_winner() if self.count >= 5 else None
            self.print_board()
            if self.winner:
                # there is a winner
                print(f"Player {self.winner} is the winner!\n")

            # switches player and increments count
            self.count += 1
            self.switch_player()

        if not self.winner:
            # there is a tie
            print(f"There's no winner. Try again!\n")
            self.winner = 'Tie'

        self.stats.save_game(self.player_1, self.player_2, self.count, self.winner)
        for player in (self.player_1, self.player_2):
            self.stats.player_stats(player)
            self.stats.global_result(player)

        self.new_game()

    def new_game (self):
        """Prompts the option to start a new game after completion."""

        while self.resume not in ['Y', 'N', 'y', 'n']:
            # sanity checks the input and changes the status of resume
            self.resume = input("Would you like a new game? Y for yes and N for no.\n")

        if self.resume.upper() == 'Y':
            # resets game status if user wants a new one
            self.reset_game()
        else:
            sys.exit("So long!")

    def reset_game (self):
        """Resets the game to its initial state."""

        self.board = None
        self.make_board()
        self.winner = None
        self.count = 0
        self.resume = False


class Human:
    def __init__ (self, player):
        """Initializes a human player that inputs moves."""

        self.symbol = player
        self.type = 'Human'
        self.name = self.type + self.symbol
        self.get_name()

    def get_name (self):
        """Prompts the user to give themselves a name."""

        try:
            self.name = input(f"Give yourself a cool name, {self.symbol}.\n")
        except ValueError:
            # recursive call to prompt a valid name
            print(f"I mean a cool name, {self.symbol}.\n")
            return self.get_name()

    def get_move (self, board):
        """Prompts the user to make the next move.
        Validates it and updates it to the board."""

        move = input(f"Make your move, fellow player {self.symbol}.\n")

        if not move.isdigit() or int(move) not in range(1, 10):
            # check if the input is the correct type
            print(f"Make your move as a numerical number in the range 1-9.\n")
            return self.get_move(board)
        else:
            move = int(move)

        # conversion from integer to 2d location
        row = int((move - 1) / 3)
        column = int((move - 1) % 3)

        if board[row][column]:
            # check if the move is on an available place of the board
            print(f"{move} is taken -- make your move in an available spot.\n")
            return self.get_move(board)

        # updates move to the board in Game class through an instance
        # board.update_board(row, column, self._player) how to make this work?
        return row, column


class Bot:
    def __init__ (self, player):
        """Initializes a bot player that takes random moves."""

        self.symbol = player
        self.type = 'Bot'
        self.name = self.type + self.symbol
        self.get_name()

    def get_name (self):
        """Prompts the user to give themselves a name."""

        try:
            self.name = input(f"Give yourself a cool name, {self.symbol}.\n")
        except ValueError:
            # recursive call to prompt a valid name
            print(f"I mean a cool name, {self.symbol}.\n")
            return self.get_name()

    def get_move (self, board):
        """Chooses a random spot to move from available candidates."""

        # algorithm for the bot to pick a random move from available spots
        avail = [(row, col) for row in range(3) for col in range(3) if not board[row][col]]
        selection = random.choice(avail)

        print(f"Player {self.symbol} made a move. Go!")

        # updates move to the board in Game class through an instance
        return selection[0], selection[1]


class Stats:
    def __init__ (self):
        """Initializes the data analysis module for the game."""

        self.path = "./stats/results_log.csv"
        self.data = None
        self.read_game()

        self.users = None
        self.rank = None

    def read_game (self):
        """Reads existing csv or initiates one for each new game."""

        try:
            self.data = pd.read_csv(self.path)
        except FileNotFoundError:
            # builds a new dataframe if there isn't one
            self.data = pd.DataFrame(columns=[
                "Game ID",
                "Player X",
                "Name X",
                "Player O",
                "Name O",
                "Move",
                "Winning Side",
                "Winner Name",
            ])

    def save_game (self, player_1, player_2, count, winner):
        """Updates csv after each game with custom statistics."""

        index = len(self.data)
        # information to attach
        self.data.loc[index] = {
            "Game ID": index + 1,
            "Player X": player_1.type,
            "Name X": player_1.name,
            "Player O": player_2.type,
            "Name O": player_2.name,
            "Move": count,
            # displaying winner symbol and name to facilitate ranking
            "Winning Side": winner,
            "Winner Name": player_1.name if winner == 'X' else player_2.name if winner == 'O' else '',
        }

        self.data.to_csv(self.path, index=False)

    def player_stats (self, player):
        """Calculates stats for each player, including total games, wins, losses and rates."""

        # using conditional statements to extract boolean values and calculate sums
        player_total = (self.data['Name X'] == player.name) | (self.data['Name O'] == player.name)
        player_win = (self.data['Winner Name'] == player.name)
        player_loss = (
                player_total &
                (self.data['Winner Name'] != player.name) &
                (self.data['Winning Side'] != 'Tie')
        )
        player_win_pct = sum(player_win) / sum(player_total)

        print(f"-----------------------\n"
              f"Summary for Player {player.symbol}\n"
              f"-----------------------\n"
              f"You have played {sum(player_total)} games in total, {player.name}.\n"
              f"You have achieved a winning rate of {player_win_pct:.2%}, "
              f"accounting for {sum(player_win)} winning games.\n"
              f"You have unfortunately lost {sum(player_loss)} games. Keep up the momentum!\n")

    def global_result (self, player):
        """Calculates stats for global user ranking, winning side ratios, etc."""

        output = input("Would you like a peek at the global results? Y for yes.\n")

        if output in ['Y', 'y']:
            # calculates total users
            self.users = set(chain(self.data['Name X'], self.data['Name O']))

            # sorts the winners first by alphabet then by total wins in descending order
            self.rank = self.data['Winner Name'].value_counts(dropna=True) \
                .sort_index().sort_values(ascending=False).index
            rank_list = list(self.rank)
            user_rank = rank_list.index(player.name) + 1

            print(f"=======================\n"
                  f"  Global Game Summary\n"
                  f"=======================\n"
                  f"In total, {len(self.data['Game ID'])} games have been played.\n"
                  f"There are {len(self.users)} users, and you currently rank No. {user_rank}.\n"
                  f"{'Congratulations, you nailed it!' if user_rank <= 3 else 'Keep up the good work!'}\n\n"
                  )

    def winner_ratio (self):
        """Counts the occurrences of winner symbols and plots them on a bar chart."""

        ratio = self.data['Winning Side'].value_counts()

        fig, ax = plt.subplots(figsize=(12, 8))
        ratio.plot.bar(rot=0, color=['crimson', 'darkgreen', 'darkgreen'])

        ax.set_xlabel('Winner')
        ax.set_ylabel('Number of Wins')
        ax.set_title('Winner Distribution', fontsize=18)
        plt.bar_label(ax.containers[0], label_type='edge')

        plt.show()

    def bot_order (self):
        """Counts the results of double bot games and plots them on a pie chart."""

        both_bot = self.data[(self.data['Player X'] == 'Bot') & (self.data['Player O'] == 'Bot')]
        ratio_bot = both_bot['Winning Side'].value_counts(normalize=True) * 100

        fig, ax = plt.subplots(figsize=(12, 8))
        patches, texts, pcts = ax.pie(
                ratio_bot, labels=['X', 'O', 'Tie'], autopct='%.1f%%',
                wedgeprops={'linewidth': 3.0, 'edgecolor': 'white'},
                textprops={'size': 'x-large'},
                startangle=90)

        for i, patch in enumerate(patches):
            texts[i].set_color(patch.get_facecolor())
        ax.set_title('Bot VS Bot: Is order in the play?', fontsize=18)

        plt.tight_layout()

    def human_vs_bot (self):
        """Counts the game results of human vs. bot and plots them on a bar chart."""

        human_wins = (
                (self.data['Player X'] == 'Human') & (self.data['Player O'] == 'Bot') &
                (self.data['Winning Side'] == 'X') | (self.data['Winning Side'] == 'O') &
                (self.data['Player O'] == 'Human') & (self.data['Player X'] == 'Bot')
        )
        bot_wins = (
                (self.data['Player X'] == 'Human') & (self.data['Player O'] == 'Bot') &
                (self.data['Winning Side'] == 'O') | (self.data['Winning Side'] == 'X') &
                (self.data['Player O'] == 'Human') & (self.data['Player X'] == 'Bot')
        )
        ties = (
                (self.data['Winning Side'] == 'Tie') &
                ((self.data['Player O'] == 'Human') & (self.data['Player X'] == 'Bot') |
                 (self.data['Player X'] == 'Human') & (self.data['Player O'] == 'Bot'))
        )

        count = [sum(human_wins), sum(bot_wins), sum(ties)]
        result = ['Human Wins', 'Bot Wins', 'Ties']
        palette = ['orange', 'darkblue', 'darkblue']

        plt.figure(figsize=(12, 8))
        plt.bar(result, count, width=0.5, color=palette)

        plt.xlabel('Results')
        plt.ylabel('Number of Games')
        plt.title('Human VS Bot: Who wins more?', fontsize=18)

        plt.show()
