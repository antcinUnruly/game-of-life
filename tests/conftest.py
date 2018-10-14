import pytest
from conway.game import Game
from conway.cell import Cell


@pytest.fixture(scope="module")
def arrange_game():
    game = Game()
    cell = Cell()
