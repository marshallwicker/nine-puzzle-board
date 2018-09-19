import sys


class NinePuzzleBoard:
    """
    A 9-puzzle board.

    Note: Instances are immutable
    """

    DIRECTIONS = frozenset(('U', 'R', 'D', 'L'))  # U - up, R - right, etc.

    _TILES = frozenset('12345678 ')  # valid chars in a configuration string

    _MOVES = 'RD|RDL|DL|URD|URDL|UDL|UR|URL|UL'.split('|')

    _MOVE_TRANSLATIONS = {'U': -3, 'R': 1, 'D': 3, 'L': -1}

    def __init__(self, board_str='12345678 '):
        """
        Initialize a new instance with tiles as given
        :param board_str: a sequence giving the location
                          of each tile.
        """
        assert set(board_str) == NinePuzzleBoard._TILES
        self._tiles = board_str
        self._blank_index = board_str.index(' ')

    def is_solvable(self):
        """
        Determine whether this board can be transformed to
        another board
        :return: True if this board can be transformed
                 to the other by sliding tiles, False
                 otherwise
        """

        inv_count = 0
        board_list = self.get_board_list()

        for i in range(8):
            for j in range(i + 1, 9):
                if i != self._blank_index and j != self._blank_index and board_list[i] > board_list[j]:
                    inv_count += 1
        return inv_count % 2 == 0

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

        new_blank = self._blank_index + self._MOVE_TRANSLATIONS[move]

        old_tile_list = list(self._tiles)

        old_tile_list[self._blank_index] = old_tile_list[new_blank]
        old_tile_list[new_blank] = ' '

        return NinePuzzleBoard(board_str=''.join(old_tile_list))

    def get_board_list(self):
        board_list = []
        for num in range(9):
            if num != self._blank_index:
                board_list.append(int(self._tiles[num]))
            else:
                board_list.append(-1)
        return board_list

    def h(self, other):
        """
        Compute a heuristic distance between this board and another
        :param other: a NinePuzzleBoard instance
        :return: a number
        """
        distance = 0
        for index, number in enumerate(self._tiles):
            other_board_index = other.get_construct_string().index(number)
            change_in_x = abs(index % 3 - other_board_index % 3)
            change_in_y = abs(index // 3 - other_board_index // 3)
            distance += change_in_x + change_in_y
        return distance

    def get_construct_string(self):
        return self._tiles

    def __eq__(self, other):
        """
        Determine whether two states are equal
        :param other: a NinePuzzleBoard instance
        :return: True iff this board and the other have
                 tiles in the same locations
        """

        return str(self) == str(other)

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

        print("Transformable?", board1.is_solvable(board2))
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

