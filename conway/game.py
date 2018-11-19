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
        if cell in self.board.alive_cells:
            self.alive(cell, neighbours_number)
            return cell

        if cell not in self.board.alive_cells:
            print('hiii')

            self.dead(cell, neighbours_number)

    def alive(self, cell, neighbours_number):
        if neighbours_number == 1:
            self.board.alive_cells.remove(cell)
        if (neighbours_number == 2) or (neighbours_number == 3):
            pass
        if neighbours_number > 3:
            # print('print alive cells if nn > 3', self.board.alive_cells, len(self.board.alive_cells))
            # print('cell', cell)
            self.board.alive_cells.remove(cell)
            # print('print alive cells if nn > 3', self.board.alive_cells, len(self.board.alive_cells))

    def dead(self, cell, neighbours_number):
        if neighbours_number == 3:
            print('wooo')
            self.board.alive_cells.append(cell)
            # print('dead cell array', self.board.alive_cells)
