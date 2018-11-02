from conway.board import Board
from conway.cell import Cell


class TestBoard():
    def test_board_instantiation(self):
        board = Board()

        board.make_alive_cells(4)

        assert (len(board.alive_cells) == 4)

    def test_find_alive_neighbours(self):
        board = Board()

        neighbours = [True, False, True, False, True]

        # board.find_alive_neighbours(neighbours)

        assert (board.find_alive_neighbours_count(neighbours) == 3)

    def test_find_position_of_alive_neighbours(self):
        board = Board()

        neighbours = [True, False, True, False, True]

        assert (board.find_position_of_alive_neighbours(neighbours) == {0: True, 2: True, 4: True})

    def test_find_neighbours_of_alive_cell(self):
        board = Board()
        cell_1 = Cell(Initial_status=True, x=5, y=5)
        cell_2 = Cell(Initial_status=True, x=4, y=6)
        cell_3 = Cell(Initial_status=True, x=5, y=4)

        board.alive_cells = [cell_1, cell_2, cell_3]

        print(board.alive_cells)

        assert (len(board.find_neighbours_of_alive_cell(cell_1)) == 2)
