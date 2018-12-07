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
            alive_neighbours_number = len(self.board.find_neighbours_of_alive_cell(alive_cell))

            self.__run_logic(alive_cell, alive_neighbours_number)
            for n in self.board.alive_cells:
                print("Im still a neighbour of cell", alive_cell.x, alive_cell.y, ": ", n.x, n.y)
                print('----alive neighbours----')
                for cell in self.board.alive_cells:
                    tuple = (cell.x, cell.y)
                    print(tuple)
                print('--------')
        return self.new_board

    def look_for_dead_cell(self):
            dead_neighbours_of_alive_cell = {

            }

            for alive_cell in self.board.alive_cells:
                # find locations where there is not alive cell
                x = alive_cell.x
                y = alive_cell.y

                x_minus_1 = x - 1
                y_plus_1 = y + 1
                x_plus_1 = x + 1
                y_minus_1 = y - 1


                def push_cell_to_array():
                    dead_neighbours_of_alive_cell.append(alive_cell)


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

                # count_map = {}
                # for x in combinations_dictionary.keys():
                #     count_map[x] = count_map.get(x, 0) +1
                # print(count_map)
                # for key in combinations_dictionary.keys():
                #     count_map = {}
                #     count_map[key] = count_map.get(key, 0) +1
                #     print(count_map)
                # array = []
                # for key in combinations_dictionary.keys():
                #
                #     array.append(key)
                #     counter = Counter(key)
                #     print(array)





                # print('neighbours combos of cell', alive_cell.x, alive_cell.y, combinations_dictionary.keys())
                # print('dead neighbours of cell', alive_cell.x, alive_cell.y, dead_neighbours_of_alive_cell)
                # print('alive cell positions', alive_cell_positions)



    def __run_logic(self, cell, neighbours_number):
        self.look_for_dead_cell()
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
            # print('dead cell array', self.board.alive_cells)