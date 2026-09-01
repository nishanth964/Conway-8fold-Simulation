import pygame

from game import Game


def test_window_size():
    game = Game()

    assert game.width == 800
    assert game.height == 950

    pygame.quit()


def test_simulation_area():
    game = Game()

    assert game.simulationArea.width == 800
    assert game.simulationArea.height == 800
    assert game.simulationArea.topleft == (0, 0)

    pygame.quit()


def test_grid_size():
    game = Game()

    assert game.gridSize == 200
    assert game.cellSize == 4

    pygame.quit()