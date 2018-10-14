import random
from cell import Cell

class Square:
    def __init__(self, number_of_cells):
        self.cell_list = []

        for cell in range(number_of_cells):
            cell = Cell(Initial_status=bool(random.getrandbits(1)))
            self.cell_list.append(cell)


square = Square(9)

# for attr, value in vars(square).items():
#     for cell in value:
#         print(cell.status)

