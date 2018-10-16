import pytest
import numpy as np
from conway.game import Game
from conway.cell import Cell
from conway.neighbours import Neighbours


class TestGameOfLife():

    def test_fewer_than_two_live_neighbours(self):
        game = Game()

        cell = Cell(Initial_status=True)

        neighbours = Neighbours()

        neighbours.neighbour_right.status = True
        neighbours.neighbour_bottom_right.status = False
        neighbours.neighbour_bottom.status = False
        neighbours.neighbour_bottom_left.status = False
        neighbours.neighbour_left.status = False
        neighbours.neighbour_top_left.status = False
        neighbours.neighbour_top.status = False
        neighbours.neighbour_top_right.status = False

        game.run(cell, neighbours.list)

        assert (cell.status == False)

    def test_two_live_neighbours(self):
        game = Game()

        cell = Cell(Initial_status=True)

        neighbours = Neighbours()

        neighbours.neighbour_right.status = True
        neighbours.neighbour_bottom_right.status = True
        neighbours.neighbour_bottom.status = False
        neighbours.neighbour_bottom_left.status = False
        neighbours.neighbour_left.status = False
        neighbours.neighbour_top_left.status = False
        neighbours.neighbour_top.status = False
        neighbours.neighbour_top_right.status = False

        game.run(cell, neighbours.list)
        assert (cell.status == True)

    def test_three_live_neighbours(self):
        game = Game()
        cell = Cell(Initial_status=True)

        neighbours = Neighbours()

        neighbours.neighbour_right.status = True
        neighbours.neighbour_bottom_right.status = True
        neighbours.neighbour_bottom.status = True
        neighbours.neighbour_bottom_left.status = False
        neighbours.neighbour_left.status = False
        neighbours.neighbour_top_left.status = False
        neighbours.neighbour_top.status = False
        neighbours.neighbour_top_right.status = False

        game.run(cell, neighbours.list)
        assert (cell.status == True)

    def test_more_than_three_live_neighbours(self):
        game = Game()

        cell = Cell(Initial_status=True)

        neighbours = Neighbours()

        neighbours.neighbour_right.status = True
        neighbours.neighbour_bottom_right.status = True
        neighbours.neighbour_bottom.status = True
        neighbours.neighbour_bottom_left.status = True
        neighbours.neighbour_left.status = False
        neighbours.neighbour_top_left.status = False
        neighbours.neighbour_top.status = False
        neighbours.neighbour_top_right.status = False

        game.run(cell, neighbours.list)
        assert (cell.status == False)

    def test_five_live_neighbours(self):
        game = Game()

        cell = Cell(Initial_status=True)

        neighbours = Neighbours()

        neighbours.neighbour_right.status = True
        neighbours.neighbour_bottom_right.status = True
        neighbours.neighbour_bottom.status = True
        neighbours.neighbour_bottom_left.status = True
        neighbours.neighbour_left.status = True
        neighbours.neighbour_top_left.status = False
        neighbours.neighbour_top.status = False
        neighbours.neighbour_top_right.status = False

        game.run(cell, neighbours.list)
        assert (cell.status == False)

    def test_dead_cell_with_three_live_neighbours(self):
        game = Game()

        cell = Cell(Initial_status=False)

        neighbours = Neighbours()

        neighbours.neighbour_right.status = True
        neighbours.neighbour_bottom_right.status = True
        neighbours.neighbour_bottom.status = True
        neighbours.neighbour_bottom_left.status = False
        neighbours.neighbour_left.status = False
        neighbours.neighbour_top_left.status = False
        neighbours.neighbour_top.status = False
        neighbours.neighbour_top_right.status = False

        game.run(cell, neighbours.list)
        assert (cell.status == True)

    def test_status_of_neighbour_cell(self):
        cell = Cell(Initial_status=True)

        neighbours = Neighbours()

        neighbours.neighbour_right.status = False
        neighbours.neighbour_bottom_right.status = False
        neighbours.neighbour_bottom.status = True
        neighbours.neighbour_bottom_left.status = False
        neighbours.neighbour_left.status = True
        neighbours.neighbour_top_left.status = False
        neighbours.neighbour_top.status = False
        neighbours.neighbour_top_right.status = False

        game = Game()
        game.run(cell, neighbours.list)
        assert (cell.status == True)

    def test_get_count_of_alive_neighbours(self):
        # cell = Cell(Initial_status=True)

        neighbours = Neighbours()

        neighbours.neighbour_right.status = False
        neighbours.neighbour_bottom_right.status = False
        neighbours.neighbour_bottom.status = True
        neighbours.neighbour_bottom_left.status = False
        neighbours.neighbour_left.status = True
        neighbours.neighbour_top_left.status = False
        neighbours.neighbour_top.status = False
        neighbours.neighbour_top_right.status = False

        game = Game()
        count_of_alive_neighbours = game.get_count_of_alive_neighbours(neighbours.list)

        assert (count_of_alive_neighbours == 2)
