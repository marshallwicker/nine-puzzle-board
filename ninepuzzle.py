import sys


class NinePuzzleBoard:
    """
    A 9-puzzle board.

    Note: Instances are immutable
    """

    DIRECTIONS = frozenset(('U', 'R', 'D', 'L'))  # U - up, R - right, etc.

    _TILES = frozenset('12345678 ')  # valid chars in a configuration string

    _MOVES = 'RD|RDL|DL|URD|URDL|UDL|UR|URL|UL'.split('|')

    def __init__(self, board_str='12345678-'):
        """
        Initialize a new instance with tiles as given
        :param board_str: a sequence giving the location
                          of each tile.
        """
        assert set(board_str) == NinePuzzleBoard._TILES
        self._tiles = board_str
        self._blank_index = board_str.index(' ')

    def transformable_to(self, other):
        """
        Determine whether this board can be transformed to
        another board
        :param other: another board
        :return: True if this board can be transformed
                 to the other by sliding tiles, False
                 otherwise
        """
        # TODO
        return False   # STUB

    def moves(self):
        """
        Return a set of moves that this board can make
        :return: A subset of NinePuzzleBoard.DIRECTIONS that
                 reflects the direction(s) the blank can
                 be moved.
        """

        return set(self._MOVES[self._blank_index])

    def next_board(self, move):
        """
        Generate a new board configuration based on a move
        :param move: an item in NinePuzzleBoard.DIRECTIONS
        :return: a board in which the blank has been moved
                 in the given direction
        """
        assert move in self.moves(), "Invalid move: " + move

        new_blank = -1

        if move == 'U':
            new_blank = self._blank_index - 3
        elif move == 'R':
            new_blank = self._blank_index + 1
        elif move == 'D':
            new_blank = self._blank_index + 3
        elif move == 'L':
            new_blank = self._blank_index - 1

        old_tile_list = list(self._tiles)

        old_tile_list[self._blank_index] = old_tile_list[new_blank]
        old_tile_list[new_blank] = ' '

        return NinePuzzleBoard(board_str=''.join(old_tile_list))  # STUB

    def h(self, other):
        """
        Compute a heuristic distance between this board and another
        :param other: a NinePuzzleBoard instance
        :return: a number
        """
        # TODO
        return 100  # STUB

    def __eq__(self, other):
        """
        Determine whether two states are equal
        :param other: a NinePuzzleBoard instance
        :return: True iff this board and the other have
                 tiles in the same locations
        """

        return hash(self) == hash(other)

    def __str__(self):
        """
        Printable string
        :return: a string with numbers on three lines
        """
        return '\n'.join('  '.join(self._tiles[i:i+3]) for i in (0, 3, 6))

    def __hash__(self):
        return hash(self._tiles)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {} <board1> <board2>'.format(sys.argv[0]),
              file=sys.stderr)
    try:
        board1 = NinePuzzleBoard(sys.argv[1])
        print(board1)
        print()

        board2 = NinePuzzleBoard(sys.argv[2])
        print(board2)
        print()

        print("Transformable?", board1.transformable_to(board2))
        print()

        print('Hashes: ', hash(board1), hash(board2))
        print('Moves:', board1.moves())

        # Try some moves
        board = board1
        print("A sequence of moves on board:")
        print(board)
        for move in board.moves():
            try:
                next_board = board.next_board(move)
                print('After move', move)
                print(next_board)

                board = next_board
            except AssertionError:
                print('Move', move, 'is invalid')
    except AssertionError:
        print("A board configuration must have nine characters,", file=sys.stderr)
        print("each of the digits 1 through 9 and a space character.", file=sys.stderr)

