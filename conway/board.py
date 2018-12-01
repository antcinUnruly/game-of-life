import numpy as np
from random import *

from .cell import Cell


class Board:

    def __init__(self, alive_cells):
        self.alive_cells = alive_cells

    # def __init__(self, cells):
    #     self.cells_list = cells

    def make_alive_cells(self, cell_count):
        for cell in range(cell_count):
            cell = Cell(x=randint(0, 100), y=randint(0, 100))
            self.alive_cells.append(cell)
        return self.alive_cells

    def find_neighbours_of_alive_cell(self, cell):
        print('Finding  neighbours of alive cell with coordinates', cell.x, cell.y)
        x = cell.x
        y = cell.y

        x_minus_1 = x - 1
        y_plus_1 = y + 1
        x_plus_1 = x + 1
        y_minus_1 = y - 1

        neighbours_of_alive_cell = []

        for alive_cell in self.alive_cells:
            # ref code:
            # http://blog.tplus1.com/blog/2007/06/24/using-dictionaries-rather-than-complex-if-elif-else-clauses/
            def push_cell_to_array():
                print('pushing', [(alive_cell.x, alive_cell.y)], 'to neighbours_of_alive_cell array')
                neighbours_of_alive_cell.append(alive_cell)


            def do_nothing():
                for i in [x_minus_1, x, x_plus_1]:
                    for j in [y_minus_1, y, y_plus_1]:
                        if x == i and y == j:
                            continue

            # for n in neighbours_of_alive_cell:
            #     tuple = (n.x, n.y)
            #     array=[]
            #     array.append(tuple)


            combinations_dictionary = {
                (x_minus_1, y_plus_1): push_cell_to_array,
                (x, y_plus_1): push_cell_to_array,
                (x_plus_1, y_plus_1): push_cell_to_array,
                (x_minus_1, y): push_cell_to_array,
                (x_plus_1, y): push_cell_to_array,
                (x_minus_1, y_minus_1): push_cell_to_array,
                (x, y_minus_1): push_cell_to_array,
                (x_plus_1, y_minus_1): push_cell_to_array,
                (x, y): do_nothing
            }

            alive_cell_positions = (alive_cell.x, alive_cell.y)
            a = combinations_dictionary.setdefault(alive_cell_positions, do_nothing)
            dictionary_function = (combinations_dictionary[alive_cell_positions])
            dictionary_function()





        return neighbours_of_alive_cell