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
