from conway.board import Board
from conway.cell import Cell


class TestBoard:
    def test_board_instantiation(self):
        alive_cells = []
        board = Board(alive_cells)

        board.make_alive_cells(4)

        assert (len(board.alive_cells) == 4)

