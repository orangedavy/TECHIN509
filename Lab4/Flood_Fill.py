"""
File:           Flood_Fill.py
Creator:        Davy Guo
Date:           10/31/2022
Description:    This program implements a function that replaces the adjacent locations with new values when given a board 
                and a 2D location to start with.
"""

from typing import List

# board = [
#     "......................",
#     "......##########......",
#     "......#........#......",
#     "......#........#......",
#     "......#........#####..",
#     "....###............#..",
#     "....#............###..",
#     "....##############....",
# ]

board = [
    "........######........",
    "......##......##......",
    "......#........#......",
    ".....#.........#......",
    "......#........#####..",
    ".....#.............#..",
    "......#...........#...",
    ".......#.........#....",
    "........###....##.....",
    "...........####.......",
]

# convert each row of immutable string to list of strings
board = [[ele for ele in row] for row in board]

# sanity check
assert all(len(row) == len(board[0]) for row in board), f"The board should have lines of equal length."

def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    """Returns board with old values replaced with new values
    through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str])
        old (str): Value to be replaced
        new (str): Value that replaces the old
        x (int): X-coordinate of the flood start point
        y (int): Y-coordinate of the flood start point
    Returns:
        List[str]: Modified board
    """

    # validity check
    x_max, y_max = len(input_board) - 1, len(input_board[0]) - 1
    if x < 0 or y < 0 or x > x_max or y> y_max: return

    current = input_board[x][y]

    if current != old or current == new:
        # validity check
        return
    else:
        # new value assignment
        input_board[x][y] = new
    
    # recursive calls for adjacent locations in four directions
    flood_fill(input_board, old, new, x + 1, y)
    flood_fill(input_board, old, new, x - 1, y)
    flood_fill(input_board, old, new, x, y + 1)
    flood_fill(input_board, old, new, x, y - 1)

    return [''.join(row) for row in input_board]

modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

for a in modified_board:
    print(a)
