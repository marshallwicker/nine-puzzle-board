import unittest
import ninepuzzle


class NinePuzzleUnitTest(unittest.TestCase):
    BOARD_STRING = (
        ' 12345678',
        '1 2345678',
        '12 345678',
        '123 45678',
        '1234 5678',
        '12345 678',
        '123456 78',
        '1234567 8',
        '12345678 '
    )

    BOARD_STR = (
        '   1  2\n3  4  5\n6  7  8',
        '1     2\n3  4  5\n6  7  8',
        '1  2   \n3  4  5\n6  7  8',
        '1  2  3\n   4  5\n6  7  8',
        '1  2  3\n4     5\n6  7  8',
        '1  2  3\n4  5   \n6  7  8',
        '1  2  3\n4  5  6\n   7  8',
        '1  2  3\n4  5  6\n7     8',
        '1  2  3\n4  5  6\n7  8   '
    )

    def setUp(self):
        self._puzzles = [
            ninepuzzle.NinePuzzleBoard(board)
            for board in NinePuzzleUnitTest.BOARD_STRING
        ]

    def test_init(self):
        """
        Check the initial configurations by checking
        NinePuzzleBoard.__str_()
        :return: None
        """
        print('***** test_init()')

        for i, puzzle in enumerate(self._puzzles):
            self.assertEqual(str(puzzle),
                             NinePuzzleUnitTest.BOARD_STR[i],
                             'Problem with str(NinePuzzleBoard({}))'.format(
                                 repr(NinePuzzleUnitTest.BOARD_STRING[i]))
                             )

    _MOVES = 'RD RDL DL URD URDL UDL UR URL UL'.split()

    def test_moves(self):
        """
        Check that NinePuzzleBoard.moves() returns a correct value
        :return: None
        """

        print('***** test_moves()')

        for dirs, board in zip(NinePuzzleUnitTest._MOVES, self._puzzles):
            print('\n    Check', dirs, 'on board')
            print(board)
            self.assertEqual(set(dirs), board.moves())

    def test_transformable_to(self):
        """
        Check the operation of NinePuzzleBoard.transformable_to()
        :return: None
        """
        # If N is odd, then puzzle instance is solvable if number of
        # inversions is even in the input state.

        print('***** test_transformable_to()')

        test_data = [
            ('182 43765', 10),  # See https://www.geeksforgeeks.org/check-instance-8-puzzle-solvable/
            ('812 43765', 11),
            ('53472 618', 13),
            ('7215 8634', 14),
            ('146 72583', 10),
            ('16483725 ', 13),
            ('2674385 1', 15),
            ('8 6712354', 18),
            (' 46382751', 17),
            ('53216 874', 11),
            ('51234867 ', 6),
            ('5 6237184', 13),
            (' 17482365', 12),
            (' 47638521', 20),
            ('142 67853', 9),
            ('7358 4126', 17),
            ('762 15438', 15),
            ('2413568 7', 4),
            ('12345678 ', 0)
        ]

        goal_puzzle = ninepuzzle.NinePuzzleBoard('12345678 ')
        print('Goal state:')
        print(goal_puzzle)
        print()

        for board_str, count in test_data:
            test_puzzle = ninepuzzle.NinePuzzleBoard(board_str)
            print('\nTransformable from?')
            print(test_puzzle)
            result = test_puzzle.is_solvable()
            print('-->')
            print(result)
            self.assertEqual(result, count % 2 == 0)

    def test_next_board(self):
        """
        Check NinePuzzleBoard.next_board(move)
        :return: None
        """
        # Results are checked using the str(puzzle_board).

        print('***** test_next_board()')

        # Generate all possible moves

        goal_puzzle = ninepuzzle.NinePuzzleBoard('12345678 ')
        print('Goal state:')
        print(goal_puzzle)
        print()

        test_data = (
            (' 12345678', 'D', '312 45678'),
            (' 12345678', 'R', '1 2345678'),
            ('1 2345678', 'L', ' 12345678'),
            ('1 2345678', 'D', '1423 5678'),
            ('1 2345678', 'R', '12 345678'),
            ('12 345678', 'L', '1 2345678'),
            ('12 345678', 'D', '12534 678'),
            ('123 45678', 'U', ' 23145678'),
            ('123 45678', 'R', '1234 5678'),
            ('123 45678', 'D', '123645 78'),
            ('1234 5678', 'U', '1 3425678'),
            ('1234 5678', 'D', '1234756 8'),
            ('1234 5678', 'L', '123 45678'),
            ('1234 5678', 'R', '12345 678'),
            ('12345 678', 'U', '12 453678'),
            ('12345 678', 'D', '12345867 '),
            ('12345 678', 'L', '1234 5678'),
            ('123456 78', 'U', '123 56478'),
            ('123456 78', 'R', '1234567 8'),
            ('1234567 8', 'L', '123456 78'),
            ('1234567 8', 'U', '1234 6758'),
            ('12345678 ', 'U', '12345 786'),
            ('12345678 ', 'L', '1234567 8')
        )

        for board_str, move, expected_board_str in test_data:
            test_puzzle = ninepuzzle.NinePuzzleBoard(board_str)
            print('\nStart')
            print(test_puzzle)
            result_puzzle = test_puzzle.next_board(move)
            print('Move {}-->'.format(repr(move)))
            print(result_puzzle)
            self.assertEqual(result_puzzle,
                             ninepuzzle.NinePuzzleBoard(expected_board_str))

    def test_h(self):
        """
        Check that h() returns a sum of displacements measured
        as Manhattan distance
        :return: None
        """

        print('***** test_h()')

        test_data = (
            ('182 43765', 12),
            ('812 43765', 14),
            ('53472 618', 16),
            ('7215 8634', 18),
            ('146 72583', 14),
            ('16483725 ', 16),
            ('2674385 1', 18),
            ('8 6712354', 20),
            (' 46382751', 18),
            ('53216 874', 12),
            ('51234867 ', 14),
            ('5 6237184', 18),
            (' 17482365', 20),
            (' 47638521', 24),
            ('142 67853', 14),
            ('7358 4126', 16),
            ('762 15438', 16),
            ('2413568 7', 12),
            ('12345678 ', 0),
        )
        goal_puzzle = ninepuzzle.NinePuzzleBoard('12345678 ')
        print('Goal state:')
        print(goal_puzzle)
        print()

        for board_str, dist in test_data:
            test_puzzle = ninepuzzle.NinePuzzleBoard(board_str)
            print(test_puzzle)
            print('.h() -->')
            result = test_puzzle.h(goal_puzzle)
            print(result)
            self.assertEqual(result, dist)
