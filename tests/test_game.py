from game import Game


def test_grid_size():
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