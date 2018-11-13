import numpy as np
from .cell import Cell
from .board import Board


# from square import square


class Game:

    def __init__(self, board):
        self.board = board

    def run(self):
        # board = Board()
        for alive_cell in self.board.alive_cells:
            print('printing alive cell from board', alive_cell.x, alive_cell.y)
            alive_neighbours_number = len(self.board.find_neighbours_of_alive_cell(alive_cell))
            self.__run_logic(alive_cell, alive_neighbours_number)

    def __run_logic(self, cell, neighbours_number):
        if True:
            self.alive(cell, neighbours_number)
            return cell

        if cell.is_dead():
            self.dead(cell, neighbours_number)
            return cell

    def alive(self, cell, neighbours_number):
        if neighbours_number == 1:
            self.board.alive_cells.remove(cell)
        if (neighbours_number == 2) or (neighbours_number == 3):
            cell.is_alive()
        if neighbours_number > 3:
            cell.die()

    def dead(self, cell, neighbours_number):
        if neighbours_number == 3:
            cell.is_alive()

