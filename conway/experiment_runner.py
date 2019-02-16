from conway.game import Game

class ExperimentRunner:
    def __init__(self, game):
        self.game = game
        self.result = game.run()