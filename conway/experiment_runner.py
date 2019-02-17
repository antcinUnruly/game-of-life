from conway.game import Game
import numpy
import matplotlib.pyplot as plt

class ExperimentRunner:
    def __init__(self):
        self.game = None

        # print('board', game.board.alive_cells)
        # for x in game.board.alive_cells:
        #     print(x.x, x.y)
        # # print('new board', game.run().alive_cells)

    def run_experiment(self):
        self.game = Game(None)
        for x in self.game.board.alive_cells:
            print(x.x, x.y)
        #
        # print('hi', self.game.board.alive_cells)
        return self.game.run()



def main():

        experiment = ExperimentRunner()

        result = experiment.run_experiment()

        print(result)


main()