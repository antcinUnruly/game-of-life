from conway.board import Board


class TestBoard():
    def test_board_instantiation(self):
        board = Board()

        board.make_alive_cells(4)

        assert (len(board.alive_cells) == 4)


    def test_board_instantiation(self):
        board = Board()

        board.make_alive_cells(5)

        assert (len(board.alive_cells) == 5)


    def test_find_alive_neighbours(self):
        board = Board()

        neighbours = [True, False, True, False, True]

        # board.find_alive_neighbours(neighbours)

        assert(board.find_alive_neighbours_count(neighbours) == 3)

    def test_find_position_of_alive_neighbours(self):
        board = Board()

        neighbours = [True, False, True, False, True]

        assert(board.find_position_of_alive_neighbours(neighbours) == {0: True, 2: True, 4: True})