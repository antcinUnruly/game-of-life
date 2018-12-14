import numpy as np
from .cell import Cell
from .board import Board
from collections import Counter


# from square import square


class Game:

    def __init__(self, board):
        self.board = board
        self.new_board = None

    def run(self):
        self.new_board = Board()
        # board = Board()
        for alive_cell in self.board.alive_cells:
            print('collecting neighbours of alive cell with coordinates', alive_cell.x, alive_cell.y)
            alive_neighbours_number = len(self.find_neighbours_of_alive_cell(alive_cell))

            self.__run_logic(alive_cell, alive_neighbours_number)
        print('empty board', self.new_board.alive_cells)
        return self.new_board

    def find_neighbours_of_alive_cell(self, cell):
        print('Finding  neighbours of alive cell with coordinates', cell.x, cell.y)
        x = cell.x
        y = cell.y

        x_minus_1 = x - 1
        y_plus_1 = y + 1
        x_plus_1 = x + 1
        y_minus_1 = y - 1

        neighbours_of_alive_cell = []

        for alive_cell in self.board.alive_cells:
            # ref code:
            # http://blog.tplus1.com/blog/2007/06/24/using-dictionaries-rather-than-complex-if-elif-else-clauses/
            def push_cell_to_array():
                print('pushing', [(alive_cell.x, alive_cell.y)], 'to neighbours_of_alive_cell array')
                neighbours_of_alive_cell.append(alive_cell)

            def do_nothing():
                pass

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

    def __run_logic(self, cell, neighbours_number):
        if cell in self.board.alive_cells:
            self.alive(cell, neighbours_number)
            return cell

    def alive(self, cell, neighbours_number):
        if neighbours_number == 1:
            pass
        if (neighbours_number == 2) or (neighbours_number == 3):
            self.new_board.alive_cells.append(cell)
        if neighbours_number > 3:
            pass

    def dead(self, cell, neighbours_number):

        if neighbours_number == 3:
            print('wooo')
            self.new_board.alive_cells.append(cell)
