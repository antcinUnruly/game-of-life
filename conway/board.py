class Board:

    def __init__(self):
        self.alive_cells = []

    def make_alive_cells(self, cell_count):
        x = 0
        while x < cell_count:
            self.alive_cells.extend([x])
            x+=1

        # return cell_count
