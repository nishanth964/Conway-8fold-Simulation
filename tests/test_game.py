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


def test_grid_data_size():

    game = Game()

    assert len(game.grid) == 200
    assert len(game.grid[0]) == 200

    pygame.quit()


def test_cells_start_dead():

    game = Game()

    assert game.get_cell(0, 0) == 0
    assert game.get_cell(100, 100) == 0
    assert game.get_cell(199, 199) == 0

    pygame.quit()


def test_set_cell():

    game = Game()

    game.set_cell(10, 20, 1)

    assert game.get_cell(10, 20) == 1

    pygame.quit()


def test_screen_to_grid():

    game = Game()

    row, column = game.screen_to_grid(80, 40)

    assert row == 10
    assert column == 20

    pygame.quit()


def test_count_neighbors():

    game = Game()

    game.set_cell(10, 10, 1)
    game.set_cell(10, 11, 1)
    game.set_cell(11, 10, 1)

    assert game.count_neighbors(11, 11) == 3

    pygame.quit()


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

    pygame.quit()


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

    pygame.quit()


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

    pygame.quit()


def test_simulation_state():

    game = Game()

    assert game.simulation_running is False
    assert game.generation == 0
    assert game.generation_interval == 0.5
    assert game.generation_timer == 0

    pygame.quit()


def test_buttons():

    game = Game()

    assert game.startButton.width == 100
    assert game.startButton.height == 40

    assert game.stopButton.width == 100
    assert game.stopButton.height == 40

    assert game.restartButton.width == 100
    assert game.restartButton.height == 40

    assert game.stepButton.width == 100
    assert game.stepButton.height == 40

    pygame.quit()


def test_speed_slider():

    game = Game()

    assert game.slider.width == 200
    assert game.slider.height == 10

    assert game.slider_min == 0.05
    assert game.slider_max == 1.0
    assert game.slider_value == 0.5

    pygame.quit()


def test_slider_update():

    game = Game()

    game.update_slider(game.slider.left)

    assert game.generation_interval == 1.0

    game.update_slider(game.slider.right)

    assert abs(game.generation_interval - 0.05) < 0.000001

    pygame.quit()


def test_generation_counter():

    game = Game()

    assert game.generation == 0

    game.next_generation()
    game.generation += 1

    assert game.generation == 1

    pygame.quit()


def test_restart_state():

    game = Game()

    game.set_cell(10, 10, 1)
    game.generation = 5
    game.generation_timer = 0.3
    game.simulation_running = True

    # Simulate restart
    game.simulation_running = False

    game.grid = [[0 for _ in range(game.gridSize)] for _ in range(game.gridSize)]

    game.generation = 0
    game.generation_timer = 0

    assert game.simulation_running is False
    assert game.generation == 0
    assert game.generation_timer == 0
    assert game.get_cell(10, 10) == 0

    pygame.quit()
