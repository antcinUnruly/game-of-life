class Board:

    def __init__(self):
        self.alive_cells = []

    def make_alive_cells(self, cell_count):
        for x in cell_count:
            self.alive_cells.extend([x])

        # return cell_count
