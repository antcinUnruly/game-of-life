import pytest
from conway.conway import Game
from conway.cell import Cell


@pytest.fixture(scope="module")
def arrange_game():
    game = Game()
    cell = Cell()
