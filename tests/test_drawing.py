import pygame

from controls import Controls
from drawing import Drawing
from grid import Grid


def create_drawing():

    pygame.init()

    window = pygame.Surface((800, 950))

    control_area = pygame.Rect(0, 800, 800, 150)

    font = pygame.font.Font(None, 24)

    return Drawing(window, 800, control_area, font)


def test_drawing_initialization():

    drawing = create_drawing()

    assert drawing.window.get_width() == 800
    assert drawing.window.get_height() == 950
    assert drawing.simulationSize == 800

    pygame.quit()


def test_draw_cells():

    drawing = create_drawing()

    grid = Grid(200, 800)

    grid.set_cell(10, 10, 1)

    drawing.draw_cells(grid, 0)

    pygame.quit()


def test_cell_color():

    drawing = create_drawing()

    color = drawing.get_cell_color(10, 10, 0, 0)

    assert len(color) == 3

    for value in color:

        assert 0 <= value <= 255

    pygame.quit()


def test_draw_grid():

    drawing = create_drawing()

    grid = Grid(200, 800)

    drawing.draw_grid(grid)

    pygame.quit()


def test_draw_controls():

    drawing = create_drawing()

    controls = Controls()

    drawing.draw_controls(controls, 0, False)

    pygame.quit()


def test_draw_boundary():

    drawing = create_drawing()

    simulation_area = pygame.Rect(0, 0, 800, 800)

    drawing.draw_boundary(simulation_area)

    pygame.quit()
