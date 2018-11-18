import pytest
import numpy as np
from conway.game import Game
from conway.cell import Cell
from conway.board import Board


# from conway.neighbours import Neighbours


class TestGameOfLife():

    def test_fewer_than_two_live_neighbours(self):
        cell = Cell(x=1, y=1)
        neighbour1 = Cell(x=1, y=2)

        cells_list = [cell, neighbour1]

        board = Board(cells_list)

        game = Game(board)

        game.run()

        assert (cell not in board.alive_cells)

    def test_two_live_neighbours(self):
        cell = Cell(x=1, y=1)
        neighbour1 = Cell(x=1, y=2)
        neighbour2 = Cell(x=2, y=2)

        cells_list = [cell, neighbour1, neighbour2]

        board = Board(cells_list)

        game = Game(board)

        game.run()

        assert (cell in board.alive_cells)

    def test_three_live_neighbours(self):
        cell = Cell(x=1, y=1)
        neighbour1 = Cell(x=2, y=1)
        neighbour2 = Cell(x=2, y=2)
        neighbour3 = Cell(x=2, y=1)

        cells_list = [cell, neighbour1, neighbour2, neighbour3]

        board = Board(cells_list)

        game = Game(board)

        game.run()

        assert (cell in board.alive_cells)

    def test_more_than_three_live_neighbours(self):
        cell = Cell(x=1, y=1)
        neighbour1 = Cell(x=0, y=2)
        neighbour2 = Cell(x=2, y=2)
        neighbour3 = Cell(x=2, y=1)
        neighbour4 = Cell(x=0, y=0)

        cells_list = [cell, neighbour1, neighbour2, neighbour3, neighbour4]

        board = Board(cells_list)

        game = Game(board)

        game.run()

        assert (cell not in board.alive_cells)


def test_five_live_neighbours(self):
    cell = Cell(x=1, y=1)
    neighbour1 = Cell(x=1, y=2)
    neighbour2 = Cell(x=2, y=2)
    neighbour3 = Cell(x=2, y=1)
    neighbour4 = Cell(x=1, y=2)
    neighbour5 = Cell(x=0, y=0)

    cells_list = [cell, neighbour1, neighbour2, neighbour3, neighbour4, neighbour5]

    board = Board(cells_list)

    game = Game(board)

    game.run()

    assert (cell not in board.alive_cells)


def test_dead_cell_with_three_live_neighbours(self):
    cell = Cell(x=1, y=1)

    neighbour1 = Cell(x=1, y=2)
    neighbour2 = Cell(x=2, y=2)
    neighbour3 = Cell(x=2, y=1)

    cells_list = [neighbour1, neighbour2, neighbour3]

    board = Board(cells_list)

    game = Game(board)

    game.run()

    print('test dead cell array', board.alive_cells)
    print(cell in board.alive_cells)

    assert (cell in board.alive_cells)
