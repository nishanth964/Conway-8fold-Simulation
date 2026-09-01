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


def test_grid_data_size():
    game = Game()

    assert len(game.grid) == 200
    assert len(game.grid[0]) == 200


def test_cells_start_dead():
    game = Game()

    assert game.get_cell(0, 0) == 0
    assert game.get_cell(100, 100) == 0
    assert game.get_cell(199, 199) == 0


def test_set_cell():
    game = Game()

    game.set_cell(10, 20, 1)

    assert game.get_cell(10, 20) == 1


def test_screen_to_grid():
    game = Game()

    row, column = game.screen_to_grid(80, 40)

    assert row == 10
    assert column == 20

def test_count_neighbors():
    game = Game()

    game.set_cell(10, 10, 1)
    game.set_cell(10, 11, 1)
    game.set_cell(11, 10, 1)

    assert game.count_neighbors(11, 11) == 3

def test_block():
    game = Game()

    game.set_cell(10, 10, 1)
    game.set_cell(10, 11, 1)
    game.set_cell(11, 10, 1)
    game.set_cell(11, 11, 1)

    game.next_generation()

    assert game.get_cell(10, 10) == 1
    assert game.get_cell(10, 11) == 1
    assert game.get_cell(11, 10) == 1
    assert game.get_cell(11, 11) == 1

def test_blinker():
    game = Game()

    game.set_cell(10, 9, 1)
    game.set_cell(10, 10, 1)
    game.set_cell(10, 11, 1)

    game.next_generation()

    assert game.get_cell(9, 10) == 1
    assert game.get_cell(10, 10) == 1
    assert game.get_cell(11, 10) == 1

    assert game.get_cell(10, 9) == 0
    assert game.get_cell(10, 11) == 0

def test_glider():
    game = Game()

    # Initial glider
    game.set_cell(10, 11, 1)
    game.set_cell(11, 12, 1)
    game.set_cell(12, 10, 1)
    game.set_cell(12, 11, 1)
    game.set_cell(12, 12, 1)

    # Advance 4 generations
    for _ in range(4):
        game.next_generation()

    # Glider should have moved one cell down and right
    assert game.get_cell(11, 12) == 1
    assert game.get_cell(12, 13) == 1
    assert game.get_cell(13, 11) == 1
    assert game.get_cell(13, 12) == 1
    assert game.get_cell(13, 13) == 1

def test_simulation_state():
    game = Game()

    assert game.simulation_running is True
    assert game.generation == 0
    assert game.generation_interval == 0.5
    assert game.generation_timer == 0