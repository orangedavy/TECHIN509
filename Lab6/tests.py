import unittest
import logic


class TestLogic(unittest.TestCase):

    def test_check_turn (self):
        self.assertEqual(logic.check_first_turn('X'), 'X')
        self.assertEqual(logic.check_first_turn('o'), 'O')  # upper case

        self.assertRaises(ValueError, logic.check_first_turn, 123)  # not str
        self.assertRaises(ValueError, logic.check_first_turn, [10])  # not str

    def test_check_move (self):
        board = [
            ['X', None, 'O'],
            [None, None, None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.check_move(5, 'X', board), [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ])

        board = [
            ['O', 'X', 'O'],
            ['X', 'X', 'O'],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.check_move(7, 'X', board), [
            ['O', 'X', 'O'],
            ['X', 'X', 'O'],
            ['X', 'O', 'X'],
        ])

        board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        self.assertEqual(logic.check_move(9, 'O', board), [
            [None, None, None],
            [None, None, None],
            [None, None, 'O'],
        ])

        board = [
            ['X', None, 'O'],
            [None, None, None],
            [None, 'O', 'X'],
        ]
        self.assertRaises(ValueError, logic.check_move, 10, 'X', board)  # out of range
        self.assertRaises(TypeError, logic.check_move, [10], 'X', board)  # not int
        self.assertRaises(ValueError, logic.check_move, '10', 'X', board)  # not int
        self.assertRaises(ValueError, logic.check_move, 8, 'X', board)  # taken

    def test_get_winner (self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')

        board = [
            ['X', 'O', 'O'],
            ['O', 'X', 'X'],
            ['X', 'O', 'O'],
        ]
        self.assertEqual(logic.get_winner(board), None)

        board = [
            ['X', None, None],
            [None, None, None],
            [None, 'O', None],
        ]
        self.assertEqual(logic.get_winner(board), None)

        board = [
            ['X', 'X', 'X'],
            ['O', 'X', 'O'],
            ['O', 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')

        board = [
            [None, 'O', None],
            [None, 'X', None],
            [None, 'O', None],
        ]
        self.assertEqual(logic.get_winner(board), None)

    def test_switch_player (self):
        player = 'X'
        self.assertEqual(logic.switch_player(player), 'O')

        player = 'O'
        self.assertEqual(logic.switch_player(player), 'X')


if __name__ == '__main__':
    unittest.main()
