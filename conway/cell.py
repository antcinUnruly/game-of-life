class Cell:
    position_x = 0
    position_y = 0

    def __init__(self, x, y):
        self.position_x = x
        self.position_y = y

    def die(self, list):
        list.remove(self)

