# Snake Game Project

This project contains three different variations of the classic Snake game developed using Python and Pygame.

## Prerequisites

*   Python 3.x
*   Pygame library

To install Pygame, run:

```bash
pip install pygame
```

## Game Files & Modes

### 1. Snake Game (Main)
**File:** `snake_game.py`

This is the main version of the game which appears to be feature-rich.
*   **Controls:** Supports both Arrow Keys and Mouse/Touch controls (based on internal settings).
*   **Features:** Includes different grid layouts (Normal, Dhiraj, Vedant).

### 2. Snake Free Mode (Different Control)
**File:** `snake_free mode_different_control.py`

A variation where the snake can pass through walls and reappear on the other side (Wrap-around).
*   **Controls:** **Mouse Movement**. The screen is divided into diagonal quadrants. Moving the mouse into a quadrant changes the snake's direction.
    *   Top quadrant: Up
    *   Bottom quadrant: Down
    *   Left quadrant: Left
    *   Right quadrant: Right

### 3. Snake Box Mode
**File:** `Snake_box mode.py`

The classic version of Snake played within a bounded box.
*   **Controls:** **Arrow Keys**.
*   **Gameplay:** Hitting the walls or yourself typically results in a game over.

## How to Run

Navigate to the project directory in your terminal and run the desired python file.

Example:

```bash
python snake_game.py
```

or

```bash
python "Snake_box mode.py"
```

## Assets

The game relies on the following assets being in the same directory:
*   `icon.png`
*   `background.png` (Used in the main game)
*   `apple.png` / `APPLE.jpg` (Used for game elements)

## Author & Contact

*   **Author:** Manya Jain
*   **Contact:** cs1240351@iitd.ac.in

