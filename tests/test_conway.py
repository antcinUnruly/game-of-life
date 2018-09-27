import pytest
import numpy as np
from conway.conway import Game
from conway.cell import Cell


class TestGameOfLife():

    def test_fewer_than_two_neighbours(self):
        # arrange
        game = Game()
        cell = Cell(Initial_status=True)

        # act
        # cell.status = True
        new_cell = game.run(cell, 1)
        # assert
        assert (new_cell.status == False)

    def test_two_neighbours(self):
        # arrange
        game = Game()
        cell = Cell(True)
        # act
        # cell.status = True
        new_cell = game.run(cell, 2)
        # assert
        assert (new_cell.status == True)

    def test_three_neighbours(self):
        # arrange
        game = Game()
        cell = Cell(Initial_status=True)
        # act
        # cell.status = True
        new_cell = game.run(cell, 3)
        # assert
        assert (new_cell.status == True)

    def test_more_than_three_neighbours(self):
        # arrange
        game = Game()
        cell = Cell(Initial_status=True)
        # act
        # cell.status = True
        new_cell = game.run(cell, 4)
        # assert
        assert (new_cell.status == False)

    def test_five_neighbours(self):
        # arrange
        game = Game()
        cell = Cell(Initial_status=True)
        # act
        # cell.status = True
        new_cell = game.run(cell, 5)
        # assert
        assert (new_cell.status == False)

    def test_dead_cell_with_three_neighbours(self):
        game = Game()
        cell = Cell(Initial_status=False)
        # cell.status = False
        new_cell = game.run(cell, 3)
        assert (new_cell.status == True)

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

        observed_square = [cell, cell_to_right, cell_to_bottom_right,
                           cell_to_bottom, cell_to_bottom_left, cell_to_left,
                           cell_to_top_left, cell_to_top, cell_to_top_right]

        game = Game()
        game.run(cell, np.count_nonzero(observed_square))
        print("test1", np.count_nonzero(observed_square))

        assert (cell.status == False)


    def test_get_count_of_alive_neighbours(self):
        cell = Cell(Initial_status=True)
        cell_to_right = Cell(Initial_status=False)
        cell_to_bottom_right = Cell(Initial_status=False)
        cell_to_bottom = Cell(Initial_status=True)
        cell_to_bottom_left = Cell(Initial_status=False)
        cell_to_left = Cell(Initial_status=True)
        cell_to_top_left = Cell(Initial_status=False)
        cell_to_top = Cell(Initial_status=False)
        cell_to_top_right = Cell(Initial_status=False)

        observed_square = [cell, cell_to_right, cell_to_bottom_right,
                           cell_to_bottom, cell_to_bottom_left, cell_to_left,
                           cell_to_top_left, cell_to_top, cell_to_top_right]

        game = Game()
        count_of_alive_neighbours = game.get_count_of_alive_neighbours(observed_square)

        assert(count_of_alive_neighbours == 3)

