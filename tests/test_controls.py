from controls import Controls


def test_controls_initialization():

    controls = Controls()

    assert controls.startButton.width == 100
    assert controls.startButton.height == 40

    assert controls.stopButton.width == 100
    assert controls.stopButton.height == 40

    assert controls.restartButton.width == 100
    assert controls.restartButton.height == 40

    assert controls.stepButton.width == 100
    assert controls.stepButton.height == 40


def test_slider_initialization():

    controls = Controls()

    assert controls.slider.width == 200
    assert controls.slider.height == 10

    assert controls.slider_min == 0.05
    assert controls.slider_max == 1.0
    assert controls.slider_value == 0.5

    assert controls.slider_dragging is False

    assert controls.slider_area.width == 220
    assert controls.slider_area.height == 50


def test_slider_update_left():

    controls = Controls()

    value = controls.update_slider(controls.slider.left)

    assert value == controls.slider_max


def test_slider_update_right():

    controls = Controls()

    value = controls.update_slider(controls.slider.right)

    assert value == controls.slider_min


def test_slider_update_middle():

    controls = Controls()

    middle = controls.slider.centerx

    value = controls.update_slider(middle)

    assert round(value, 2) == 0.53


def test_slider_clamps_left():

    controls = Controls()

    value = controls.update_slider(-100)

    assert value == controls.slider_max


def test_slider_clamps_right():

    controls = Controls()

    value = controls.update_slider(1000)

    assert value == controls.slider_min
