import numpy as np
from random import *

from .cell import Cell


class Board:

    def __init__(self, alive_cells=[]):
        self.alive_cells = alive_cells


    # def __init__(self, cells):
    #     self.cells_list = cells

    def make_alive_cells(self, cell_count):
        for cell in range(cell_count):
            cell = Cell(x=randint(0, 100), y=randint(0, 100))
            self.alive_cells.append(cell)
        return self.alive_cells

