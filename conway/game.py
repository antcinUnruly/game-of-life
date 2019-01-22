import numpy as np
from .cell import Cell
from .board import Board
from collections import Counter


class Game:
    def __init__(self, board):
        self.board = board
        self.new_board = None

    def run(self):
        self.new_board = Board()
        del self.new_board.alive_cells[:]

        self.apply_alive_rules()
        self.apply_dead_rules()

        return self.new_board

    def apply_alive_rules(self):
        for alive_cell in self.board.alive_cells:
            alive_neighbours_number = len(self.find_neighbours_of_alive_cell(alive_cell))

            self.__run_logic(alive_cell, alive_neighbours_number)

    def apply_dead_rules(self):
        all_potential_neighbours = []

        for alive_cell in self.board.alive_cells:
            self.build_potential_neighbours_and_reincarnate_cell(all_potential_neighbours, alive_cell)

    def build_potential_neighbours_and_reincarnate_cell(self, all_potential_neighbours, alive_cell):
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
        flattened_list_of_all_potential_neighbours = [val for sublist in all_potential_neighbours for val in
                                                      sublist]
        neighbours_of_alive_cell = flattened_list_of_all_potential_neighbours

        cell_counter = Counter(neighbours_of_alive_cell)

        for key, value in cell_counter.items():
            if value == 3:
                born_cell = Cell(x=key[0], y=key[1])
                self.new_board.alive_cells.append(born_cell)

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
