import numpy as np
from .cell import Cell


# from square import square


class Game:


    def __init__(self):
        self.cells = []

    def get_count_of_alive_neighbours(self, neighbours):
        counter = 0
        for cell in neighbours:
            if cell:
                counter += 1
        return counter

    def run(self, cell, neighbours):
        alive_neighbours_number = self.get_count_of_alive_neighbours(neighbours)
        print('number of alive neighbours', alive_neighbours_number)
        self.__run_logic(cell, alive_neighbours_number)

    def __run_logic(self, cell, neighbours_number):
        if cell.is_alive():
            self.alive(cell, neighbours_number)
            print('in logic', cell, neighbours_number)
            return cell

        if cell.is_dead():
            self.dead(cell, neighbours_number)
            return cell

    def alive(self, cell, neighbours_number):
        if neighbours_number == 1:
            cell.die()
        if (neighbours_number == 2) or (neighbours_number == 3):
            cell.is_alive()
            return cell
        if neighbours_number > 3:
            cell.die()

    def dead(self, cell, neighbours_number):
        if neighbours_number == 3:
            cell.status = True
            return cell
