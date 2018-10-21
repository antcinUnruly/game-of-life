import numpy as np

class Board:

    def __init__(self):
        self.alive_cells = []

    def make_alive_cells(self, cell_count):
        x = 0
        while x < cell_count:
            self.alive_cells.extend([True])
            x += 1

        # return cell_count

    def find_alive_neighbours_count(self, neighbours):
        return(np.count_nonzero(neighbours))

    def find_position_of_alive_neighbours(self, neighbours):
        x = {k:v for k,v in enumerate(neighbours) if v == True}
        return x