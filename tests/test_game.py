from conway.game import Game
from conway.cell import Cell
from conway.board import Board
from random import *
import itertools
import pytest


class TestGameOfLife:

    def test_fewer_than_two_live_neighbours(self):
        cell = Cell(x=1, y=1)
        neighbour1 = Cell(x=1, y=2)

        cells_list = [cell, neighbour1]

        board = Board(cells_list)

        game = Game(board, 10, None)

        new_board = game.run()

        assert (cell not in new_board.alive_cells)

    def test_two_live_neighbours_one(self):
        cell = Cell(x=1, y=1)
        neighbour1 = Cell(x=1, y=2)
        neighbour2 = Cell(x=1, y=0)

        cells_list = [cell, neighbour1, neighbour2]

        board = Board(cells_list)

        game = Game(board, 10, None)

        new_board = game.run()

        assert (cell in new_board.alive_cells)
        assert (len(new_board.alive_cells) == 3)

    def test_three_live_neighbours(self):
        cell = Cell(x=1, y=1)
        neighbour1 = Cell(x=2, y=1)
        neighbour2 = Cell(x=2, y=2)
        neighbour3 = Cell(x=1, y=2)

        cells_list = [cell, neighbour1, neighbour2, neighbour3]

        board = Board(cells_list)

        game = Game(board, 10, None)

        new_board = game.run()

        assert (cell in new_board.alive_cells)

    def test_more_than_three_live_neighbours(self):
        cell = Cell(x=1, y=1)
        neighbour1 = Cell(x=0, y=2)
        neighbour2 = Cell(x=2, y=2)
        neighbour3 = Cell(x=2, y=1)
        neighbour4 = Cell(x=0, y=0)

        cells_list = [cell, neighbour1, neighbour2, neighbour3, neighbour4]

        board = Board(cells_list)

        game = Game(board, 10, None)

        new_board = game.run()

        assert (cell not in new_board.alive_cells)

    def test_dead_cell_with_three_live_neighbours(self):
        alive_cell_1 = Cell(x=0, y=1)
        alive_cell_2 = Cell(x=1, y=2)
        alive_cell_3 = Cell(x=2, y=1)

        cells_list = [alive_cell_1, alive_cell_2, alive_cell_3]

        board = Board(cells_list)

        game = Game(board, 10, None)

        new_board = game.run()

        assert (len(new_board.alive_cells) == 2)
        test = [t for t in new_board.alive_cells if t.x == 1 and t.y == 1]
        assert (test[0].x == 1)
        assert (test[0].y == 1)

    def test_find_neighbours_of_alive_cell(self):
        cell_1 = Cell(x=1, y=1)
        cell_2 = Cell(x=2, y=2)
        cell_3 = Cell(x=2, y=1)

        alive_cells = [cell_1, cell_2, cell_3]
        board = Board(alive_cells)

        game = Game(board, 10, None)

        assert (len(game.find_neighbours_of_alive_cell(cell_1)) == 2)

    def test_check_correct_neighbours_of_alive_cell(self):
        cell_1 = Cell(x=5, y=5)
        cell_2 = Cell(x=4, y=6)
        cell_3 = Cell(x=5, y=4)

        alive_cells = [cell_1, cell_2, cell_3]
        board = Board(alive_cells)

        game = Game(board, 10, None)

        assert (game.find_neighbours_of_alive_cell(cell_1) == [cell_2, cell_3])

    def test_run_game_twice(self):
        alive_cell_1 = Cell(x=0, y=1)
        alive_cell_2 = Cell(x=1, y=2)
        alive_cell_3 = Cell(x=2, y=1)

        cells_list = [alive_cell_1, alive_cell_2, alive_cell_3]

        board = Board(cells_list)

        game = Game(board, 10, None)

        new_board = game.run()
        assert (len(new_board.alive_cells) == 2)
        test = [t for t in new_board.alive_cells if t.x == 1 and t.y == 1]
        assert (test[0].x == 1)
        assert (test[0].y == 1)

        new_board2 = game.run()

        for x in new_board.alive_cells:
            print('newboard', x.x, x.y)

        for x in new_board2.alive_cells:
            print('newboard2', x.x, x.y)

        assert (len(new_board2.alive_cells) == 0)

    def test_run_game_two_adjacent_cells(self):
        alive_cell_1 = Cell(x=1, y=1)
        alive_cell_2 = Cell(x=1, y=2)

        cells_list = [alive_cell_1, alive_cell_2]

        board = Board(cells_list)

        game = Game(board, 10, None)

        new_board = game.run()
        assert (len(new_board.alive_cells) == 0)

    def test_assess_length_of_game_board_alive_cells_array(self):
        seed(10)

        number_of_cells_on_board = 10
        upper_limit = 10

        game = Game(None, upper_limit, number_of_cells_on_board)

        assert (len(game.board.alive_cells) == 10)

    def test_make_alive_cells(self):
        seed(10)

        number_of_cells_on_board = 20
        upper_limit = 20

        game = Game(None, upper_limit, number_of_cells_on_board)

        for a, b in itertools.combinations(game.board.alive_cells, 2):
            if a.x == b.x and a.y == b.y:
                assert (a not in game.board.alive_cells)

        assert (len(game.board.alive_cells) == 20)

    def test_randomisation_of_cell_coordinates(self):
        seed(10)

        randint(0, 20)

        for x in range(0, 40):
            print(randint(0, 20))

    def test_check_for_duplicates(self):
        alive_cell_1 = Cell(x=0, y=1)
        alive_cell_2 = Cell(x=1, y=2)
        alive_cell_3 = Cell(x=2, y=1)
        alive_cell_4 = Cell(x=2, y=1)

        cells_list = [alive_cell_1, alive_cell_2, alive_cell_3, alive_cell_4]

        board = Board(cells_list)

        game = Game(board)

        flag = True

        assert (game.check_for_duplicates(
            game.board.alive_cells) == flag)

    def test_upper_limit_constraint_fail(self):
        with pytest.raises(ValueError):
            seed(10)

            number_of_cells_on_board = 15
            upper_limit = 2

            game = Game(None, upper_limit, number_of_cells_on_board)

    def test_upper_limit_constraint_success(self):
        seed(10)

        number_of_cells_on_board = 15
        upper_limit = 8

        game = Game(None, upper_limit, number_of_cells_on_board)
        assert (game.board is not None)
        # game.raise_upper_limit_constraint()

    # write a test for game over; run a test for a game that doesn't last long

    # write a test for displaying a message or some visual prompt to user
