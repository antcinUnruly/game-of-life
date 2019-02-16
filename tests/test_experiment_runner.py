from conway.experiment_runner import ExperimentRunner
from conway.game import Game
import numpy
import matplotlib.pyplot as plt
from math import log

class TestExperimentRunner:
    def test_run_experiment(self):
        game = Game(None)
        experiment = ExperimentRunner(game)

        result = experiment.game.run()

        # for x in result.alive_cells:
        #     print(x.x, x.y)
        #
        # print(result.alive_cells)


        assert(result.alive_cells == [])
