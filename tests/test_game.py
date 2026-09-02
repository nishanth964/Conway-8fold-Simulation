from game import Game


def test_window_size():

    game = Game()

    assert game.width == 800
    assert game.height == 950


def test_simulation_area():

    game = Game()

    assert game.simulationArea.width == 800
    assert game.simulationArea.height == 800


def test_simulation_state():

    game = Game()

    assert game.simulation_running is False
    assert game.generation == 0
    assert game.generation_interval == 0.5


def test_generation_counter():

    game = Game()

    assert game.generation == 0

    game.grid.next_generation()

    game.generation += 1

    assert game.generation == 1


def test_restart_state():

    game = Game()

    game.grid.set_cell(10, 10, 1)

    game.generation = 5

    game.simulation_running = True

    game.restart()

    assert game.grid.get_cell(10, 10) == 0

    assert game.generation == 0

    assert game.simulation_running is False

    assert game.generation_timer == 0


def test_drawing_state():

    game = Game()

    assert game.is_drawing is False
    assert game.last_drawn_cell is None


def test_drawing_cell():

    game = Game()

    game.grid.set_symmetric_cell(90, 110, 1)

    assert game.grid.get_cell(90, 110) == 1
