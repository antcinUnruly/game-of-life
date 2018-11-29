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

            print('alive cell - collecting neighbours', alive_cell.x, alive_cell.y)

            # print('printing alive cell from board', alive_cell.x, alive_cell.y)

            neighbours = self.find_neighbours_of_alive_cell(self.board, alive_cell)
            for n in neighbours:
                print("Im still a neighbour of cell", alive_cell.x, alive_cell.y, ": ", n.x, n.y)

            alive_neighbours_number = len(neighbours)
            print('number of neighbours', alive_neighbours_number)

            self.__run_logic(alive_cell, alive_neighbours_number)

    def find_neighbours_of_alive_cell(self, board, cell):


        print('Finding my neighbours', cell.x, cell.y)

        x = cell.x
        y = cell.y

        x_minus_1 = x - 1
        y_plus_1 = y + 1
        x_plus_1 = x + 1
        y_minus_1 = y - 1

        print('x: ', x)
        print('y: ', y)
        print('x_minus_1: ', x_minus_1)
        print('y_plus_1: ', y_plus_1)
        print('x_plus_1: ', x_plus_1)
        print('y_minus_1: ', y_minus_1)


        neighbours_of_alive_cell = []

        for potential_neighbour in self.board.alive_cells:
            # ref code:
            # http://blog.tplus1.com/blog/2007/06/24/using-dictionaries-rather-than-complex-if-elif-else-clauses/
            def push_cell_to_array():
                neighbours_of_alive_cell.append(potential_neighbour)

            def do_nothing():
                print('cell in exam')

            combinations_dictionary = {
                (x_minus_1, y_plus_1): push_cell_to_array,
                (x, y_plus_1): push_cell_to_array,
                (x_plus_1, y_plus_1): push_cell_to_array,
                (x_minus_1, y): push_cell_to_array,
                (x, y): do_nothing,
                (x_plus_1, y): push_cell_to_array,
                (x_minus_1, y_minus_1): push_cell_to_array,
                (x, y_minus_1): push_cell_to_array,
                (x_plus_1, y_minus_1): push_cell_to_array
            }

            alive_cell_positions = (potential_neighbour.x, potential_neighbour.y)
            a = combinations_dictionary.setdefault(alive_cell_positions, do_nothing)
            dictionary_function = (combinations_dictionary[alive_cell_positions])
            dictionary_function()
            # print('combinations dictionary keys', combinations_dictionary.keys())
            print('------')

            # for key in combinations_dictionary.keys():
            #
            #     if key == (x, y):
            #         key = alive_cell_positions
            #         print('cell in exam', key)
            #     else:
            #         print(key)
            # print('------')


        for n in neighbours_of_alive_cell:
            print("Im a neighbour of cell", x, y, ": ", n.x, n.y)

        return neighbours_of_alive_cell




    def __run_logic(self, cell, neighbours_number):
        if cell in self.board.alive_cells:
            self.alive(cell, neighbours_number)
            return cell

    def alive(self, cell, neighbours_number):
        if neighbours_number == 1:
            self.board.alive_cells.remove(cell)
        if (neighbours_number == 2) or (neighbours_number == 3):
            print('Im alive')
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
