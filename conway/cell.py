class Cell:
    position_x = 0
    position_y = 0

    def __init__(self, x, y):
        self.position_x = x
        self.position_y = y

    def die(self, cells_list):
        cells_list.remove(self)

    def is_dead(self, cells_list):
        self not in cells_list

    def is_alive(self, cells_list):
        self in cells_list
