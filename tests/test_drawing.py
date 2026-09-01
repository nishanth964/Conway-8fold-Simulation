import pygame

from drawing import Drawing
from grid import Grid
from controls import Controls


def test_drawing_initialization():

    pygame.init()

    window = pygame.Surface((800, 950))
    control_area = pygame.Rect(0, 800, 800, 150)
    font = pygame.font.Font(None, 24)

    drawing = Drawing(window, 800, control_area, font)

    assert drawing.window == window
    assert drawing.simulationSize == 800
    assert drawing.controlArea == control_area
    assert drawing.font == font

    pygame.quit()


def test_draw_cells():

    pygame.init()

    window = pygame.Surface((800, 950))
    control_area = pygame.Rect(0, 800, 800, 150)
    font = pygame.font.Font(None, 24)

    drawing = Drawing(window, 800, control_area, font)

    grid = Grid(200, 800)
    grid.set_cell(10, 10, 1)

    drawing.draw_cells(grid)

    pygame.quit()


def test_draw_grid():

    pygame.init()

    window = pygame.Surface((800, 950))
    control_area = pygame.Rect(0, 800, 800, 150)
    font = pygame.font.Font(None, 24)

    drawing = Drawing(window, 800, control_area, font)

    grid = Grid(200, 800)

    drawing.draw_grid(grid)

    pygame.quit()


def test_draw_controls():

    pygame.init()

    window = pygame.Surface((800, 950))
    control_area = pygame.Rect(0, 800, 800, 150)
    font = pygame.font.Font(None, 24)

    drawing = Drawing(window, 800, control_area, font)

    controls = Controls()

    drawing.draw_controls(controls, 0, False)

    pygame.quit()


def test_draw_boundary():

    pygame.init()

    window = pygame.Surface((800, 950))
    control_area = pygame.Rect(0, 800, 800, 150)
    font = pygame.font.Font(None, 24)

    drawing = Drawing(window, 800, control_area, font)

    simulation_area = pygame.Rect(0, 0, 800, 800)

    drawing.draw_boundary(simulation_area)

    pygame.quit()
