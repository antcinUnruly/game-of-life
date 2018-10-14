from .cell import Cell


class Neighbours:

    def __init__(self):
        self.neighbour_right = Cell(Initial_status=True)
        self.neighbour_bottom_right = Cell(Initial_status=True)
        self.neighbour_bottom = Cell(Initial_status=True)
        self.neighbour_bottom_left = Cell(Initial_status=True)
        self.neighbour_left = Cell(Initial_status=True)
        self.neighbour_top_left = Cell(Initial_status=True)
        self.neighbour_top = Cell(Initial_status=True)
        self.neighbour_top_right = Cell(Initial_status=True)

        self.list = [self.neighbour_right, self.neighbour_bottom_right, self.neighbour_bottom,
                     self.neighbour_bottom_left, self.neighbour_left, self.neighbour_top_left, self.neighbour_top,
                     self.neighbour_top_right]

    def get_neighbour_status(self, neighbour):
        return neighbour.status
