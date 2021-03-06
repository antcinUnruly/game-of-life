import pytest
import numpy as np
from conway.conway import Game
from conway.cell import Cell


class TestGameOfLife():

    def test_fewer_than_two_live_neighbours(self):
        game = Game()

        cell = Cell(Initial_status=True)
        cell_to_right = Cell(Initial_status=True)
        cell_to_bottom_right = Cell(Initial_status=False)
        cell_to_bottom = Cell(Initial_status=False)
        cell_to_bottom_left = Cell(Initial_status=False)
        cell_to_left = Cell(Initial_status=False)
        cell_to_top_left = Cell(Initial_status=False)
        cell_to_top = Cell(Initial_status=False)
        cell_to_top_right = Cell(Initial_status=False)

        # removed cell from observed_square
        observed_square = [cell_to_right, cell_to_bottom_right,
                           cell_to_bottom, cell_to_bottom_left, cell_to_left,
                           cell_to_top_left, cell_to_top, cell_to_top_right]


        game.run(cell, observed_square)

        assert (cell.status == False)

    def test_two_live_neighbours(self):
        game = Game()
        cell = Cell(Initial_status=True)
        cell_to_right = Cell(Initial_status=True)
        cell_to_bottom_right = Cell(Initial_status=True)
        cell_to_bottom = Cell(Initial_status=False)
        cell_to_bottom_left = Cell(Initial_status=False)
        cell_to_left = Cell(Initial_status=False)
        cell_to_top_left = Cell(Initial_status=False)
        cell_to_top = Cell(Initial_status=False)
        cell_to_top_right = Cell(Initial_status=False)

        observed_square = [cell_to_right, cell_to_bottom_right,
                           cell_to_bottom, cell_to_bottom_left, cell_to_left,
                           cell_to_top_left, cell_to_top, cell_to_top_right]

        game.run(cell, observed_square)
        assert (cell.status == True)

    def test_three_live_neighbours(self):
        game = Game()
        cell = Cell(Initial_status=True)
        cell_to_right = Cell(Initial_status=True)
        cell_to_bottom_right = Cell(Initial_status=True)
        cell_to_bottom = Cell(Initial_status=True)
        cell_to_bottom_left = Cell(Initial_status=False)
        cell_to_left = Cell(Initial_status=False)
        cell_to_top_left = Cell(Initial_status=False)
        cell_to_top = Cell(Initial_status=False)
        cell_to_top_right = Cell(Initial_status=False)

        observed_square = [cell_to_right, cell_to_bottom_right,
                           cell_to_bottom, cell_to_bottom_left, cell_to_left,
                           cell_to_top_left, cell_to_top, cell_to_top_right]

        game.run(cell, observed_square)
        assert (cell.status == True)

    def test_more_than_three_live_neighbours(self):
        game = Game()
        cell = Cell(Initial_status=True)
        cell_to_right = Cell(Initial_status=True)
        cell_to_bottom_right = Cell(Initial_status=True)
        cell_to_bottom = Cell(Initial_status=True)
        cell_to_bottom_left = Cell(Initial_status=True)
        cell_to_left = Cell(Initial_status=False)
        cell_to_top_left = Cell(Initial_status=False)
        cell_to_top = Cell(Initial_status=False)
        cell_to_top_right = Cell(Initial_status=False)

        observed_square = [cell_to_right, cell_to_bottom_right,
                           cell_to_bottom, cell_to_bottom_left, cell_to_left,
                           cell_to_top_left, cell_to_top, cell_to_top_right]

        game.run(cell, observed_square)
        assert (cell.status == False)

    def test_five_live_neighbours(self):
        game = Game()
        cell = Cell(Initial_status=True)
        cell_to_right = Cell(Initial_status=True)
        cell_to_bottom_right = Cell(Initial_status=True)
        cell_to_bottom = Cell(Initial_status=True)
        cell_to_bottom_left = Cell(Initial_status=True)
        cell_to_left = Cell(Initial_status=True)
        cell_to_top_left = Cell(Initial_status=True)
        cell_to_top = Cell(Initial_status=False)
        cell_to_top_right = Cell(Initial_status=False)

        observed_square = [cell_to_right, cell_to_bottom_right,
                           cell_to_bottom, cell_to_bottom_left, cell_to_left,
                           cell_to_top_left, cell_to_top, cell_to_top_right]

        game.run(cell, observed_square)
        assert (cell.status == False)

    def test_dead_cell_with_three_live_neighbours(self):
        game = Game()
        cell = Cell(Initial_status=False)
        cell_to_right = Cell(Initial_status=True)
        cell_to_bottom_right = Cell(Initial_status=True)
        cell_to_bottom = Cell(Initial_status=True)
        cell_to_bottom_left = Cell(Initial_status=False)
        cell_to_left = Cell(Initial_status=False)
        cell_to_top_left = Cell(Initial_status=False)
        cell_to_top = Cell(Initial_status=False)
        cell_to_top_right = Cell(Initial_status=False)

        observed_square = [cell_to_right, cell_to_bottom_right,
                           cell_to_bottom, cell_to_bottom_left, cell_to_left,
                           cell_to_top_left, cell_to_top, cell_to_top_right]

        game.run(cell, observed_square)
        assert (cell.status == True)

    def test_status_of_neighbour_cell(self):
        cell = Cell(Initial_status=True)
        cell_to_right = Cell(Initial_status=False)
        cell_to_bottom_right = Cell(Initial_status=False)
        cell_to_bottom = Cell(Initial_status=True)
        cell_to_bottom_left = Cell(Initial_status=False)
        cell_to_left = Cell(Initial_status=True)
        cell_to_top_left = Cell(Initial_status=False)
        cell_to_top = Cell(Initial_status=False)
        cell_to_top_right = Cell(Initial_status=False)

        observed_square = [cell_to_right, cell_to_bottom_right,
                           cell_to_bottom, cell_to_bottom_left, cell_to_left,
                           cell_to_top_left, cell_to_top, cell_to_top_right]

        game = Game()
        game.run(cell, observed_square)
        assert (cell.status == True)

    def test_get_count_of_alive_neighbours(self):
        # cell = Cell(Initial_status=True)
        cell_to_right = Cell(Initial_status=False)
        cell_to_bottom_right = Cell(Initial_status=False)
        cell_to_bottom = Cell(Initial_status=True)
        cell_to_bottom_left = Cell(Initial_status=False)
        cell_to_left = Cell(Initial_status=True)
        cell_to_top_left = Cell(Initial_status=False)
        cell_to_top = Cell(Initial_status=False)
        cell_to_top_right = Cell(Initial_status=False)

        observed_square = [cell_to_right, cell_to_bottom_right,
                           cell_to_bottom, cell_to_bottom_left, cell_to_left,
                           cell_to_top_left, cell_to_top, cell_to_top_right]

        game = Game()
        count_of_alive_neighbours = game.get_count_of_alive_neighbours(observed_square)

        assert (count_of_alive_neighbours == 2)
