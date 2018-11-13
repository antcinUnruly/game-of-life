import pytest
import numpy as np
from conway.game import Game
from conway.cell import Cell
from conway.board import Board


# from conway.neighbours import Neighbours


class TestGameOfLife():

    def test_fewer_than_two_live_neighbours(self):

        cell = Cell(x=1, y=1)
        neighbour1 = Cell( x=1, y=2)

        cells_list = [cell, neighbour1]

        board = Board(cells_list)

        game = Game(board)

        game.run()

        assert (cell not in board.alive_cells)

    def test_two_live_neighbours(self):
        game = Game()

        cell = Cell( x=1, y=1)
        neighbour1 = Cell(x=1, y=2)
        neighbour2 = Cell(x=2, y=2)

        neighbours_list = [neighbour1, neighbour2]

        game.run(cell, neighbours_list)
        assert (cell in game.cells)

    def test_three_live_neighbours(self):
        game = Game()
        cell = Cell(game, x=1, y=1)
        neighbour1 = Cell(game, x=1, y=2)
        neighbour2 = Cell(game, x=2, y=2)
        neighbour3 = Cell(game, x=2, y=1)

        neighbours_list = [neighbour1, neighbour2, neighbour3]

        game.run(cell, neighbours_list)
        assert (cell in game.cells)

    def test_more_than_three_live_neighbours(self):
        game = Game()

        cell = Cell(game, x=1, y=1)
        neighbour1 = Cell(game, x=1, y=2)
        neighbour2 = Cell(game, x=2, y=2)
        neighbour3 = Cell(game, x=2, y=1)
        neighbour4 = Cell(game, x=2, y=3)

        neighbours_list = [neighbour1, neighbour2, neighbour3, neighbour4]

        game.run(cell, neighbours_list)
        assert (cell not in game.cells)

    def test_five_live_neighbours(self):
        game = Game()

        cell = Cell(game, x=1, y=1)

        neighbour1 = Cell(game, x=1, y=2)
        neighbour2 = Cell(game, x=2, y=2)
        neighbour3 = Cell(game, x=2, y=1)
        neighbour4 = Cell(game, x=2, y=3)
        neighbour5 = Cell(game, x=3, y=3)

        neighbours_list = [neighbour1, neighbour2, neighbour3, neighbour4, neighbour5]

        game.run(cell, neighbours_list)
        assert (cell not in game.cells)

    def test_dead_cell_with_three_live_neighbours(self):
        game = Game()

        cell = Cell(game, x=1, y=1)

        neighbour1 = Cell(game, x=1, y=2)
        neighbour2 = Cell(game, x=2, y=2)
        neighbour3 = Cell(game, x=2, y=1)

        print('cell not in game.cells', cell in game.cells)

        neighbours_list = [neighbour1, neighbour2, neighbour3]

        game.run(cell, neighbours_list)

        print('cell in game.cells', cell in game.cells)

        assert (cell in game.cells)
