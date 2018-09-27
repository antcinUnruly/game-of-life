import numpy as np
from .cell import Cell


class Game:

    def get_count_of_alive_neighbours(self, observed_square):
        counter = 0
        for cell in observed_square:
            if cell.status == True:
                counter += 1
        return counter

        # count_of_true = np.count_nonzero(observed_square)
        # print(count_of_true)

        # return observed_square.count(True)

    def run2(self, cell, observed_square):
        alive_neighbours_number = self.get_count_of_alive_neighbours(observed_square)
        self.run(cell, alive_neighbours_number)

        # no neighbours number, call run, pass get_count_of_alive_neighbours
        # in run method

    def run(self, cell, neighbours_number):
        print(cell.status, neighbours_number)
        if cell.status == True:
            self.alive(cell, neighbours_number)
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
