import pytest
from conway.conway import Game
from conway.cell import Cell


class TestGameOfLife():
    def test_fewer_than_two_neighbours(self):
        # arrange
        game = Game()
        cell = Cell()
        # act
        cell.status = True
        new_cell = game.run(cell, 1)
        # assert
        assert (new_cell.status == False)

    def test_two_neighbours(self):
        # arrange
        game = Game()
        cell = Cell()
        # act
        cell.status = True
        new_cell = game.run(cell, 2)
        # assert
        assert (new_cell.status == True)

    def test_three_neighbours(self):
        # arrange
        game = Game()
        cell = Cell()
        # act
        cell.status = True
        new_cell = game.run(cell, 3)
        # assert
        assert (new_cell.status == True)

    def test_more_than_three_neighbours(self):
        # arrange
        game = Game()
        cell = Cell()
        # act
        cell.status = True
        new_cell = game.run(cell, 4)
        # assert
        assert (new_cell.status == False)

    def test_five_neighbours(self):
        # arrange
        game = Game()
        cell = Cell()
        # act
        cell.status = True
        new_cell = game.run(cell, 5)
        # assert
        assert (new_cell.status == False)

    def test_death_cell_with_more_than_three_neighbours(self):
        game = Game()
        cell = Cell()
        cell.status = False
        new_cell = game.run(cell, 3)
        assert (new_cell.status == True)
