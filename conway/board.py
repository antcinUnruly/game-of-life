import numpy as np
from random import *

from .cell import Cell


class Board:

    def __init__(self):
        self.alive_cells = []

    def make_alive_cells(self, cell_count):
        for cell in range(cell_count):
            cell = Cell(Initial_status=True, x=randint(0, 100), y=randint(0, 100))
            self.alive_cells.append(cell)
        return self.alive_cells

    def find_neighbours_of_alive_cell(self, cell):
        x = cell.position_x
        y = cell.position_y

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

            def do_nothing(*args):
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

            # print(d)

            alive_cell_positions = (alive_cell.position_x, alive_cell.position_y)
            # print(k)
            dictionary_function = (combinations_dictionary[alive_cell_positions])
            dictionary_function()

            # if alive_cell.position_x == xmin1 and alive_cell.position_y == yplus1:
            #     neighbours_of_alive_cell.append(alive_cell)
            # elif alive_cell.position_x == x and alive_cell.position_y == yplus1:
            #     neighbours_of_alive_cell.append(alive_cell)
            # elif alive_cell.position_x == xplus1 and alive_cell.position_y == yplus1:
            #     neighbours_of_alive_cell.append(alive_cell)
            # elif alive_cell.position_x == xmin1 and alive_cell.position_y == y:
            #     neighbours_of_alive_cell.append(alive_cell)
            # elif alive_cell.position_x == xplus1 and alive_cell.position_y == y:
            #     neighbours_of_alive_cell.append(alive_cell)
            # elif alive_cell.position_x == xmin1 and alive_cell.position_y == ymin1:
            #     neighbours_of_alive_cell.append(alive_cell)
            # elif alive_cell.position_x == x and alive_cell.position_y == ymin1:
            #     neighbours_of_alive_cell.append(alive_cell)
            # elif alive_cell.position_x == xplus1 and alive_cell.position_y == ymin1:
            #     neighbours_of_alive_cell.append(alive_cell)

        return neighbours_of_alive_cell

    # def __append_cell_to_neighbours_of_alive_cell(self, cell, neighbours_of_alive_cell):
    #     neighbours_of_alive_cell.append(cell)
