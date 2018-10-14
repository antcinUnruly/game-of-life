import numpy as np
from .cell import Cell
# from square import square


class Game:

    def get_count_of_alive_neighbours(self, neighbours):
        counter = 0
        for cell in neighbours:
            if cell.status == True:
                counter += 1
        return counter

        # count_of_true = np.count_nonzero(observed_square)
        # print(count_of_true)

        # return observed_square.count(True)

    def run(self, cell, neighbours):
        alive_neighbours_number = self.get_count_of_alive_neighbours(neighbours)
        print(alive_neighbours_number)
        self.__run_logic(cell, alive_neighbours_number)

        # no neighbours number, call run, pass get_count_of_alive_neighbours
        # in run method

    def __run_logic(self, cell, neighbours_number):

        if cell.status == True:
            self.alive(cell, neighbours_number)
            print(cell.status, neighbours_number)
            return cell

        if cell.status == False:
            self.dead(cell, neighbours_number)
            return cell

    def alive(self, cell, neighbours_number):
        if neighbours_number == 1:
            cell.status = False
            return cell
        if (neighbours_number == 2) or (neighbours_number == 3):
            cell.status = True
            return cell
        if neighbours_number > 3:
            cell.status = False
            return cell

    def dead(self, cell, neighbours_number):
        if neighbours_number == 3:
            cell.status = True
            return cell
