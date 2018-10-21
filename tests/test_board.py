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

        print(neighbours)

        # board.find_alive_neighbours(neighbours)

        assert(board.find_alive_neighbours_count(neighbours) == 3)