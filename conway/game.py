import numpy as np
from .cell import Cell


# from square import square


class Game:
    def __init__(self):
        self.cells = []

    def get_count_of_alive_neighbours(self, neighbours):
        counter = 0
        for cell in neighbours:
            if cell in self.cells:
                counter += 1
        print(self.cells)
        return counter

    def run(self, cell, neighbours):
        alive_neighbours_number = self.get_count_of_alive_neighbours(neighbours)
        print(alive_neighbours_number)
        self.__run_logic(cell, alive_neighbours_number)

    def __run_logic(self, cell, neighbours_number):
        if cell in self.cells:
            self.alive(cell, neighbours_number)
            print(cell, neighbours_number)
            return cell

        if cell not in self.cells:
            self.dead(cell, neighbours_number)
            return cell

    def alive(self, cell, neighbours_number):
        if neighbours_number == 1:
            cell.die(self.cells)
            return cell
        if (neighbours_number == 2) or (neighbours_number == 3):
            cell.is_alive(self.cells)
            return cell
        if neighbours_number > 3:
            cell.status = False
            return cell

    def dead(self, cell, neighbours_number):
        if neighbours_number == 3:
            cell.status = True
            return cell
