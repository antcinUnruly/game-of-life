from conway.experiment_runner import ExperimentRunner
from conway.game import Game

class TestExperimentRunner:
    def test_run_experiment(self):
        game = Game(None)
        experiment = ExperimentRunner(game)

        result = experiment.result

        assert(result == game.board)
