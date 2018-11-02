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
        yminus1 = y - 1

        neighbours_of_alive_cell = []

        for alive_cell in self.alive_cells:
            if alive_cell.position_x == xmin1 and alive_cell.position_y == yplus1:
                neighbours_of_alive_cell.append(alive_cell)
            elif alive_cell.position_x == x and alive_cell.position_y == yplus1:
                neighbours_of_alive_cell.append(alive_cell)
            elif alive_cell.position_x == xplus1 and alive_cell.position_y == yplus1:
                neighbours_of_alive_cell.append(alive_cell)
            elif alive_cell.position_x == xmin1 and alive_cell.position_y == y:
                neighbours_of_alive_cell.append(alive_cell)
            elif alive_cell.position_x == xplus1 and alive_cell.position_y == y:
                neighbours_of_alive_cell.append(alive_cell)
            elif alive_cell.position_x == xmin1 and alive_cell.position_y == yminus1:
                neighbours_of_alive_cell.append(alive_cell)
            elif alive_cell.position_x == x and alive_cell.position_y == yminus1:
                neighbours_of_alive_cell.append(alive_cell)
            elif alive_cell.position_x == xplus1 and alive_cell.position_y == yminus1:
                neighbours_of_alive_cell.append(alive_cell)

        return neighbours_of_alive_cell
