import pytest
import numpy as np
from conway.game import Game
from conway.cell import Cell


# from conway.neighbours import Neighbours


class TestGameOfLife():

    def test_fewer_than_two_live_neighbours(self):
        game = Game()
        print('printing game cells', game.cells)

        cell = Cell(game, x=1, y=1)
        print('printing cell', cell)

        neighbour1 = Cell(game, x=1, y=2)
        print('printing neighbour', neighbour1)

        neighbours_list = [neighbour1]

        print('printing game cells', game.cells)
        print('is cell alive?', cell.is_alive())

        game.run(cell, neighbours_list)

        print('cells after game run', game.cells)
        print('cell is NOT in list of cells', cell not in game.cells)

        assert (cell not in game.cells)

    def test_two_live_neighbours(self):
        game = Game()

        cell = Cell(game, x=1, y=1)
        neighbour1 = Cell(game, x=1, y=2)
        neighbour2 = Cell(game, x=2, y=2)

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
