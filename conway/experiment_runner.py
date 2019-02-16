from conway.game import Game
import numpy
import matplotlib.pyplot as plt

class ExperimentRunner:
    def __init__(self, game):
        self.game = game

        print(len(self.game.board.alive_cells))
        for x in self.game.board.alive_cells:
            print(x.x, x.y)

