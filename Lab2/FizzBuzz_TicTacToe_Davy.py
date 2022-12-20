"""

Program: FizzBuzz_TicTacToe_Davy.py
Author: Shucheng Guo
Date-Written: 10/13/2022
Description: This program solves the problem of FizzBuzz and aims to scale the problem into a bigger one.
             This program also solves the problem of Tic Tac Toe and returns the result.
"""


def fizzbuzz(n, mtp_1, mtp_2, mtp_3):

    output = []

    for i in range(1, n + 1):
        # check if the number is a multiple of 3, 5, or 7
        rmd_mtp_1, rmd_mtp_2, rmd_mtp_3 = i % mtp_1, i % mtp_2, i % mtp_3
        # append the string(s) if condition satisfied or the number
        output.append('Fizz' * (not rmd_mtp_1) + 'Buzz' * (not rmd_mtp_2) + 'Qizz' * (not rmd_mtp_3) or str(i))

    return output


# one-liner solution using list comprehension
def fizzbuzz_simp(n):

    output = ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) + 'Qizz' * (not i % 7)
              or str(i) for i in range(1, n + 1)]

    return output


def tictactoe(board):

    # convert text strings to int values for easier calculation and comparison
    mod_board = [[0 if ele == 'O' else 1 if ele == 'X' else ele for ele in row] for row in board]

    # sums of values in rows and columns of the board
    rows = [sum(i) for i in mod_board]
    columns = [sum(i) for i in zip(*mod_board)]

    # convert diagonal values to lists
    dec_diagonal = [mod_board[i][i] for i in range(len(mod_board))]
    inc_diagonal = [mod_board[i][len(mod_board)-1-i] for i in range(len(mod_board))]

    # concatenate sums of eight routes in a list for final check
    sum_temp = rows + columns + [sum(dec_diagonal)] + [sum(inc_diagonal)]

    # conditional result return based on the sum of each route
    return 'O won' if 0 in sum_temp else 'X won' if 3 in sum_temp else 'Draw'


if __name__ == "__main__":
    print('\n'.join(fizzbuzz(100, 3, 5, 7)))
    print('\n'.join(fizzbuzz_simp(100)))
    print(tictactoe([['O', 'X', 'X'], ['X', 'X', 'O'], ['O', 'X', 'X']]))
