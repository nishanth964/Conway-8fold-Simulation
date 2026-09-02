# Conway: 8Fold Simulation

A visual implementation of **Conway's Game of Life** built with Python and Pygame. The simulation follows the standard **B3/S23 Game of Life rules**.

Instead of a normal Game of Life simulation, this project adds **8-fold symmetry** to the way cells are placed. When you place a cell, the same cell is placed in its symmetrical positions around the center. This creates patterns that evolve while keeping their 8-fold symmetry.

## What is Conway: Game of life

Conway's Game of Life is a cellular automaton created by mathematician John Conway. It is a simulation made up of a grid of cells, where each cell can either be alive or dead. The cells change from one generation to the next depending on how many neighboring cells they have. Unlike other games this game is 0 player game

## Controls

| Control          | Function                                      |
| ---------------- | --------------------------------------------- |
| **Start**        | Start the simulation                          |
| **Stop**         | Pause the simulation                          |
| **Restart**      | Clear the simulation and reset the generation |
| **Step**         | Advance by one generation                     |
| **Speed Slider** | Adjust simulation speed                       |
| **Mouse Click/Drag**  | Add/remove symmetrical cells                  |


## Conway's Game of Life

Each cell can be either **alive** or **dead**.

For every generation:

#### Survival

A living cell survives if it has **2 or 3 neighbors**.

#### Death

A living cell dies if it has:

* Fewer than 2 neighbors — underpopulation
* More than 3 neighbors — overpopulation

#### Birth

A dead cell becomes alive if it has exactly **3 neighbors**.

These rules are commonly represented as:

**B3/S23**

* **B3** — birth with 3 neighbors
* **S23** — survival with 2 or 3 neighbors

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd Conway-8fold-Simulation
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

You can use any Python environment you prefer(if needed), such as:

* `venv`
* `conda`
* `virtualenv`

Using a virtual environment is recommended, but it is not required.

## Running the Simulation

Run the program with:

```bash
python main.py
```

A Pygame window will open with the simulation and controls.

## Running Tests

To run the test suite:

```bash
python -m pytest
```
The tests cover areas including:

* Game of Life rules
* Neighbor counting
* Blinker
* Block
* Glider
* 8-fold symmetry
* Grid boundaries
* Generation state
* Controls
* Rendering



## 8-Fold Symmetry

The main feature that differentiates this project from a standard Game of Life implementation is the symmetry system.

When a cell is placed, the program calculates its corresponding positions through:

* Horizontal reflection
* Vertical reflection
* Diagonal reflection
* Rotational symmetry

The resulting pattern is therefore mirrored around the center of the simulation.

As generations evolve, the symmetric structure produces complex, mandala-like patterns.

## Project Goal

The goal of this project is to combine the computational rules of **Conway's Game of Life** with geometric symmetry and generative visual effects.

The result is a simulation that is both a programming project and an interactive visual experiment.
