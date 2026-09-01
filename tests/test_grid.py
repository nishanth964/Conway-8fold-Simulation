from grid import Grid


def test_grid_size():

    grid = Grid(200, 800)

    assert grid.gridSize == 200
    assert grid.cellSize == 4


def test_grid_data_size():

    grid = Grid(200, 800)

    assert len(grid.grid) == 200
    assert len(grid.grid[0]) == 200


def test_cells_start_dead():

    grid = Grid(200, 800)

    assert grid.get_cell(0, 0) == 0
    assert grid.get_cell(100, 100) == 0
    assert grid.get_cell(199, 199) == 0


def test_set_cell():

    grid = Grid(200, 800)

    grid.set_cell(10, 20, 1)

    assert grid.get_cell(10, 20) == 1


def test_screen_to_grid():

    grid = Grid(200, 800)

    row, column = grid.screen_to_grid(80, 40)

    assert row == 10
    assert column == 20


def test_count_neighbors():

    grid = Grid(200, 800)

    grid.set_cell(10, 10, 1)
    grid.set_cell(10, 11, 1)
    grid.set_cell(11, 10, 1)

    assert grid.count_neighbors(11, 11) == 3


def test_block():

    grid = Grid(200, 800)

    grid.set_cell(10, 10, 1)
    grid.set_cell(10, 11, 1)
    grid.set_cell(11, 10, 1)
    grid.set_cell(11, 11, 1)

    grid.next_generation()

    assert grid.get_cell(10, 10) == 1
    assert grid.get_cell(10, 11) == 1
    assert grid.get_cell(11, 10) == 1
    assert grid.get_cell(11, 11) == 1


def test_blinker():

    grid = Grid(200, 800)

    grid.set_cell(10, 9, 1)
    grid.set_cell(10, 10, 1)
    grid.set_cell(10, 11, 1)

    grid.next_generation()

    assert grid.get_cell(9, 10) == 1
    assert grid.get_cell(10, 10) == 1
    assert grid.get_cell(11, 10) == 1

    assert grid.get_cell(10, 9) == 0
    assert grid.get_cell(10, 11) == 0


def test_glider():

    grid = Grid(200, 800)

    # Initial glider
    grid.set_cell(10, 11, 1)
    grid.set_cell(11, 12, 1)
    grid.set_cell(12, 10, 1)
    grid.set_cell(12, 11, 1)
    grid.set_cell(12, 12, 1)

    # Advance 4 generations
    for _ in range(4):
        grid.next_generation()

    # Glider should have moved one cell down and right
    assert grid.get_cell(11, 12) == 1
    assert grid.get_cell(12, 13) == 1
    assert grid.get_cell(13, 11) == 1
    assert grid.get_cell(13, 12) == 1
    assert grid.get_cell(13, 13) == 1


def test_clear():

    grid = Grid(200, 800)

    grid.set_cell(10, 10, 1)

    grid.clear()

    assert grid.get_cell(10, 10) == 0
