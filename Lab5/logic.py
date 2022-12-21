# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.

def make_empty_board ():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


def prompt_input (intent, player=None):
    """Prompts user input with different intents for display."""

    prompt = {
        'turn': f"Choose the player, X or O?\n",
        'move': f"Make your move, player {player}.\n",
    }
    return input(prompt[intent])


def print_board (board, winner):
    """Prints the current status of the board and total scores."""

    # convert the board for better display
    mod_board = [col if col else " " for row in board for col in row]

    print(f"Tic-tac-toe Scoreboard\n\n"
          f"\t  {mod_board[0]} | {mod_board[1]} | {mod_board[2]}  \n"
          f"\t ———|———|——— \t\n"
          f"\t  {mod_board[3]} | {mod_board[4]} | {mod_board[5]}  \n"
          f"\t ———|———|——— \t\n"
          f"\t  {mod_board[6]} | {mod_board[7]} | {mod_board[8]}  \n"
          f"\nCurrent winner: {winner}")


def check_first_turn (turn):
    """Sanity checks the input of the first turn."""

    try:
        turn = str(turn).upper()
    except ValueError or TypeError:
        # check if the input is the correct type
        print("Enter a letter.")
        return check_first_turn(prompt_input('turn'))

    if turn not in ['X', 'O']:
        # check if the player is chosen as either X or O
        print("Please pick a valid letter.")
        return check_first_turn(prompt_input('turn'))

    return turn


def check_move (move, player, board):
    """Sanity checks the move of the player.
    Updates the board status if passed."""

    try:
        move = int(move)
    except TypeError:
        # check if the input is the correct type
        print("Enter a digit.")
        return check_move(prompt_input('move', player), player, board)

    # convert the move to the form of row and column for double index
    remainder = move % 3
    row = move // 3 if remainder else move // 3 - 1
    column = remainder - 1 if remainder else 2

    if move not in range(1, 10):
        # check if the move is expressed as an integer and in the valid range
        print("Please make your move as a numerical number in the range 1-9.")
        return check_move(prompt_input('move', player), player, board)

    if board[row][column] is not None:
        # check if the move is on an available place of the board
        print("Please make your move in an available place.")
        return check_move(prompt_input('move', player), player, board)

    # update the status of the place to player info if the move is valid
    board[row][column] = player

    return board


def get_winner (board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""

    # convert text strings to int values for easier calculation and comparison
    mod_board = [[-1 if ele == 'O' else 1 if ele == 'X' else 0 for ele in row]
                 for row in board]

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


def switch_player (player):
    """Given the character for a player, returns the other player."""
    return "O" if player == "X" else "X"
