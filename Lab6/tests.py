import unittest
import logic
from unittest.mock import patch


class TestLogic(unittest.TestCase):

    def test_get_winner (self):
        game = logic.Game(logic.Human('X'), logic.Bot('O'))

        board_1 = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        board_2 = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        board_3 = [
            ['X', 'O', 'O'],
            ['X', 'X', 'X'],
            ['O', 'O', 'X'],
        ]
        board_4 = [
            ['X', None, None],
            [None, 'X', 'X'],
            ['O', 'O', 'O'],
        ]
        board_5 = [
            ['X', 'X', 'O'],
            ['X', 'O', 'X'],
            ['O', 'O', 'X'],
        ]
        board_6 = [
            ['X', 'X', 'O'],
            ['O', 'O', 'X'],
            ['X', 'X', 'O'],
        ]

        game.board = board_1
        self.assertEqual(game.get_winner(), None)
        game.board = board_2
        self.assertEqual(game.get_winner(), 'X')
        game.board = board_3
        self.assertEqual(game.get_winner(), 'X')
        game.board = board_4
        self.assertEqual(game.get_winner(), 'O')
        game.board = board_5
        self.assertEqual(game.get_winner(), 'O')
        game.board = board_6
        self.assertEqual(game.get_winner(), None)

    def test_switch_player (self):
        game = logic.Game(logic.Human('X'), logic.Bot('O'))

        self.assertEqual(game.player.symbol, 'X')

        game.switch_player()
        self.assertEqual(game.player.symbol, 'O')

        game.switch_player()
        self.assertEqual(game.player.symbol, 'X')

    def test_update_board (self):
        game = logic.Game(logic.Human('X'), logic.Bot('O'))

        board_1 = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        board_2 = [
            ['X', None, 'O'],
            [None, None, None],
            [None, 'O', 'X'],
        ]

        board_1_updated = [
            [None, None, None],
            [None, 'X', None],
            [None, None, None],
        ]
        board_2_updated = [
            ['X', 'X', 'O'],
            [None, None, None],
            [None, 'O', 'X'],
        ]

        game.board = board_1
        game.update_board(1, 1)
        self.assertEqual(game.board, board_1_updated)

        game.board = board_2
        game.update_board(0, 1)
        self.assertEqual(game.board, board_2_updated)

    def test_new_game (self):
        game = logic.Game(logic.Human('X'), logic.Bot('O'))

        game.resume = "Y"
        game.new_game()
        self.assertEqual(game.resume, False)

        game.resume = "N"
        with self.assertRaises(SystemExit) as new:
            game.new_game()
        self.assertEqual(new.exception.code, 'So long!')

    def test_human_get_move (self):
        human = logic.Human('X')
        board = [
            ['X', None, 'O'],
            [None, None, None],
            [None, 'O', 'X'],
        ]

        with patch('builtins.input', return_value='2'):
            self.assertEqual(human.get_move(board), (0, 1))

        with patch('builtins.input', return_value='5'):
            self.assertEqual(human.get_move(board), (1, 1))

        with patch('builtins.input', return_value='7'):
            self.assertEqual(human.get_move(board), (2, 0))


if __name__ == '__main__':
    unittest.main()
