from conway.game import Game
import numpy
# import matplotlib.pyplot as plt

# class ExperimentRunner:
#     def __init__(self):
#         self.game = Game(None)
#
#         print(len(self.game.board.alive_cells))
#
#         # print('board', game.board.alive_cells)
#         # for x in game.board.alive_cells:
#         #     print(x.x, x.y)
#         # # print('new board', game.run().alive_cells)
#
#     def run_experiment(self):
#         exp = self.game.run()
#
#         # for x in self.game.board.alive_cells:
#         #     print(x.x, x.y)
#         #
#         # #
#         # new_board = self.game.run()
#         # new_board2 = self.game.run()
#
#         # print('hi', self.game.board.alive_cells)
#         # return new_board
#         return exp
#
#
#
# def main():
#         i = 0
#         while i < 10:
#             experiment = ExperimentRunner()
#
#             result = experiment.run_experiment()
#             i +=1
#
#             print(result.alive_cells)
#             return result.alive_cells
#
#             # for x in result.alive_cells:
#             #     return('cell in ', result, x.x, x.y)
#
#
#
# main()