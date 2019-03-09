from conway.board import Board
from conway.cell import Cell


class TestBoard:
    def test_board_instantiation(self):
        alive_cell_1 = Cell(x=1, y=1)
        alive_cell_2 = Cell(x=1, y=2)

        alive_cells = [alive_cell_1, alive_cell_2]

        board = Board(alive_cells)

        assert (len(board.alive_cells) == 2)
