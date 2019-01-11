import numpy as np
from .cell import Cell
from .board import Board
from collections import Counter


# from square import square


class Game:

    def print_cells(self, arr):
        for x in arr:
            print(x.x, x.y)

    def __init__(self, board):
        self.board = board
        self.new_board = None
        print('new_board in init', self.new_board)

    def run(self):
        self.new_board = Board()
        del self.new_board.alive_cells[:]
        print('new board beginning of run', self.new_board.alive_cells)

        # board = Board()
        self.apply_alive_rules()
        self.apply_dead_rules()

        return self.new_board

    def apply_alive_rules(self):
        for alive_cell in self.board.alive_cells:
            print('collecting neighbours of alive cell with coordinates', alive_cell.x, alive_cell.y)
            alive_neighbours_number = len(self.find_neighbours_of_alive_cell(alive_cell))

            self.__run_logic(alive_cell, alive_neighbours_number)

    def apply_dead_rules(self):
        all_potential_neighbours = []
        for alive_cell in self.board.alive_cells:
            x = alive_cell.x
            y = alive_cell.y

            x_minus_1 = x - 1
            y_plus_1 = y + 1
            x_plus_1 = x + 1
            y_minus_1 = y - 1

            potential_combinations = [
                (x_minus_1, y_plus_1),
                (x, y_plus_1),
                (x_plus_1, y_plus_1),
                (x_minus_1, y),
                (x_plus_1, y),
                (x_minus_1, y_minus_1),
                (x, y_minus_1),
                (x_plus_1, y_minus_1),
            ]

            all_potential_neighbours.append(potential_combinations)
            print(len(potential_combinations))
            flattened_list_of_all_potential_neighbours = [val for sublist in all_potential_neighbours for val in
                                                          sublist]
            neighbours_of_alive_cell = flattened_list_of_all_potential_neighbours
            # print('flattened neighbours', neighbours_of_alive_cell)

            # for pair in potential_combinations:
            #     if pair == (x, y):
            #         pass
            #     else:
            #         neighbours_of_alive_cell.append(pair)
            #
            # for alive_cell in self.board.alive_cells:
            #     for cell in self.find_neighbours_of_alive_cell(alive_cell):
            #
            # neighbours_of_alive_cell.append(cell)
            #
            # self.print_cells(potential_combinations)
            #

            cell_counter = Counter(neighbours_of_alive_cell)
            print(cell_counter)
            for key, value in cell_counter.items():
                if value == 3:
                    print(alive_cell)
                    born_cell = Cell(x=key[0], y=key[1])
                    print(born_cell, born_cell.x, born_cell.y)
                    print('in apply dead rules, after counter', self.new_board.alive_cells)
                    # self.new_board.alive_cells.append(born_cell)
                    print('in apply dead rules, after counter', self.new_board.alive_cells)

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

    def find_neighbours_of_alive_cell(self, cell):
        print('Finding neighbours of alive cell with coordinates', cell.x, cell.y)
        x = cell.x
        y = cell.y

        x_minus_1 = x - 1
        y_plus_1 = y + 1
        x_plus_1 = x + 1
        y_minus_1 = y - 1

        neighbours_of_alive_cell = []
        potential_neighbours_of_alive_cell = []

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

        print('neighbours of alive cell', neighbours_of_alive_cell)
        return neighbours_of_alive_cell
