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

        # x = 0
        # while x < cell_count:
        #     cell.status = True
        #     self.alive_cells.extend(cell)
        #     x += 1

        # return cell_count

    def find_alive_neighbours_count(self, neighbours):
        return (np.count_nonzero(neighbours))

    def find_position_of_alive_neighbours(self, neighbours):
        x = {k: v for k, v in enumerate(neighbours) if v == True}
        return x

    def find_neighbours_of_alive_cell(self, cell):
        return self.alive_cells

