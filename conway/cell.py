class Cell:

    def __init__(self, game, x=0, y=0):
        self.game = game
        self.x = x
        self.y = y
        self.game.cells.append(self)

    def die(self):
        self.game.cells.remove(self)

    def is_dead(self):
        return self not in self.game.cells

    def is_alive(self):
        return self in self.game.cells
