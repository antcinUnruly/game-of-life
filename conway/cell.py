class Cell:
    status = False
    position_x = 0
    position_y = 0

    def __init__(self, Initial_status, x, y):
        self.status = Initial_status
        self.position_x = x
        self.position_y = y

