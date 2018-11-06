from conway.board import Board
from conway.cell import Cell


class TestBoard():
    def test_board_instantiation(self):
        board = Board()

        board.make_alive_cells(4)

        assert (len(board.alive_cells) == 4)

    def test_find_neighbours_of_alive_cell(self):
        board = Board()
        cell_1 = Cell(Initial_status=True, x=5, y=5)
        cell_2 = Cell(Initial_status=True, x=4, y=6)
        cell_3 = Cell(Initial_status=True, x=5, y=4)

        board.alive_cells = [cell_1, cell_2, cell_3]

        assert (len(board.find_neighbours_of_alive_cell(cell_1)) == 2)

    def test_check_correct_neighbours_of_alive_cell(self):
        board = Board()

        cell_1 = Cell(Initial_status=True, x=5, y=5)
        cell_2 = Cell(Initial_status=True, x=4, y=6)
        cell_3 = Cell(Initial_status=True, x=5, y=4)

        board.alive_cells = [cell_1, cell_2, cell_3]

        assert(board.find_neighbours_of_alive_cell(cell_1) == [cell_2, cell_3])


