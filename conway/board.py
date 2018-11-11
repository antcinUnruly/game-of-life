import numpy as np
from random import *

from .cell import Cell
from .game import Game


class Board:

    def __init__(self):
        self.alive_cells = []

    def make_alive_cells(self, cell_count):
        for cell in range(cell_count):
            game = Game()
            cell = Cell(game, x=randint(0, 100), y=randint(0, 100))
            self.alive_cells.append(cell)
        return self.alive_cells

    def find_neighbours_of_alive_cell(self, cell):
        x = cell.x
        y = cell.y

        xmin1 = x - 1
        yplus1 = y + 1
        xplus1 = x + 1
        ymin1 = y - 1

        neighbours_of_alive_cell = []

        for alive_cell in self.alive_cells:
            # ref code:
            # http://blog.tplus1.com/blog/2007/06/24/using-dictionaries-rather-than-complex-if-elif-else-clauses/
            def push_cell_to_array():
                neighbours_of_alive_cell.append(alive_cell)

            def do_nothing():
                pass

            combinations_dictionary = {
                (xmin1, yplus1): push_cell_to_array,
                (x, yplus1): push_cell_to_array,
                (xplus1, yplus1): push_cell_to_array,
                (xmin1, y): push_cell_to_array,
                (xplus1, y): push_cell_to_array,
                (xmin1, ymin1): push_cell_to_array,
                (x, ymin1): push_cell_to_array,
                (xplus1, ymin1): push_cell_to_array,
                (x, y): do_nothing

            }

            alive_cell_positions = (alive_cell.x, alive_cell.y)
            dictionary_function = (combinations_dictionary[alive_cell_positions])
            dictionary_function()

        return neighbours_of_alive_cell
