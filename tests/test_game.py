import pytest
import numpy as np
from conway.game import Game
from conway.cell import Cell


# from conway.neighbours import Neighbours


class TestGameOfLife():

    def test_fewer_than_two_live_neighbours(self):
        game = Game()

        cell = Cell(x=1, y=1)

        neighbour1 = Cell(x=1, y=2)

        # instead of having an array just for the neighbours, thought of having one cells_list array containing
        # the cell and its neighbour/s, so that then we can assert that the cell is not in the array anymore
        cells_list = [cell, neighbour1]

        game.run(cell, cells_list)

        # assert (cell.status == False)

        cell.die(cells_list)
        #assert cell is not cells list
        assert (cell not in cells_list)

    def test_two_live_neighbours(self):
        game = Game()

        cell = Cell(x=1, y=1)
        neighbour1 = Cell(x=1, y=2)
        neighbour2 = Cell(x=2, y=2)

        cells_list = [cell, neighbour1, neighbour2]

        game.run(cell, cells_list)
        assert (cell.status == True)

    def test_three_live_neighbours(self):
        game = Game()
        cell = Cell(Initial_status=True, x=1, y=1)
        neighbour1 = Cell(Initial_status=True, x=1, y=2)
        neighbour2 = Cell(Initial_status=True, x=2, y=2)
        neighbour3 = Cell(Initial_status=True, x=2, y=1)

        neighbours_list = [neighbour1, neighbour2, neighbour3]

        game.run(cell, neighbours_list)
        assert (cell.status == True)

    def test_more_than_three_live_neighbours(self):
        game = Game()

        game = Game()
        cell = Cell(Initial_status=True, x=1, y=1)
        neighbour1 = Cell(Initial_status=True, x=1, y=2)
        neighbour2 = Cell(Initial_status=True, x=2, y=2)
        neighbour3 = Cell(Initial_status=True, x=2, y=1)
        neighbour4 = Cell(Initial_status=True, x=2, y=3)

        neighbours_list = [neighbour1, neighbour2, neighbour3, neighbour4]

        game.run(cell, neighbours_list)
        assert (cell.status == False)

    def test_five_live_neighbours(self):
        game = Game()

        cell = Cell(Initial_status=True, x=1, y=1)

        neighbour1 = Cell(Initial_status=True, x=1, y=2)
        neighbour2 = Cell(Initial_status=True, x=2, y=2)
        neighbour3 = Cell(Initial_status=True, x=2, y=1)
        neighbour4 = Cell(Initial_status=True, x=2, y=3)
        neighbour5 = Cell(Initial_status=True, x=3, y=3)

        neighbours_list = [neighbour1, neighbour2, neighbour3, neighbour4, neighbour5]

        game.run(cell, neighbours_list)
        assert (cell.status == False)

    def test_dead_cell_with_three_live_neighbours(self):
        game = Game()

        cell = Cell(Initial_status=False, x=1, y=1)

        neighbour1 = Cell(Initial_status=True, x=1, y=2)
        neighbour2 = Cell(Initial_status=True, x=2, y=2)
        neighbour3 = Cell(Initial_status=True, x=2, y=1)


        neighbours_list = [neighbour1, neighbour2, neighbour3]

        game.run(cell, neighbours_list)

        assert (cell.status == True)
