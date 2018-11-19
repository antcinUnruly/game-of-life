from conway.board import Board
from conway.cell import Cell


class TestBoard:
    def test_board_instantiation(self):
        alive_cells = []
        board = Board(alive_cells)

        board.make_alive_cells(4)

        assert (len(board.alive_cells) == 4)

    def test_find_neighbours_of_alive_cell(self):
        cell_1 = Cell(x=1, y=1)
        cell_2 = Cell(x=2, y=2)
        cell_3 = Cell(x=3, y=3)

        alive_cells = [cell_1, cell_2, cell_3]
        board = Board(alive_cells)

        assert (len(board.find_neighbours_of_alive_cell(cell_1)) == 2)

    def test_check_correct_neighbours_of_alive_cell(self):
        cell_1 = Cell(x=5, y=5)
        cell_2 = Cell(x=4, y=6)
        cell_3 = Cell(x=5, y=4)
        alive_cells = [cell_1, cell_2, cell_3]
        board = Board(alive_cells)


        assert (board.find_neighbours_of_alive_cell(cell_1) == [cell_2, cell_3])
