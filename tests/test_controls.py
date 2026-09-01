import pygame

from controls import Controls


def test_buttons():

    controls = Controls()

    assert controls.startButton.width == 100
    assert controls.startButton.height == 40

    assert controls.stopButton.width == 100
    assert controls.stopButton.height == 40

    assert controls.restartButton.width == 100
    assert controls.restartButton.height == 40

    assert controls.stepButton.width == 100
    assert controls.stepButton.height == 40


def test_speed_slider():

    controls = Controls()

    assert controls.slider.width == 200
    assert controls.slider.height == 10

    assert controls.slider_min == 0.05
    assert controls.slider_max == 1.0
    assert controls.slider_value == 0.5


def test_slider_update():

    controls = Controls()

    controls.update_slider(controls.slider.left)

    assert controls.slider_value == 1.0

    controls.update_slider(controls.slider.right)

    assert abs(controls.slider_value - 0.05) < 0.000001


def test_slider_stays_inside_range():

    controls = Controls()

    controls.update_slider(0)

    assert controls.slider_value == 1.0

    controls.update_slider(1000)

    assert abs(controls.slider_value - 0.05) < 0.000001
