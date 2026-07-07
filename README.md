# Balatro Clone (Python)

A recreation of the popular roguelike poker game **Balatro**, developed in **Grade 11** using **Python**, **Pygame Zero**, and **pgzhelper**.

This project was created as a way to practice object-oriented programming, game logic, and graphical user interface development. It includes poker hand evaluation, joker effects, score calculation, animated gameplay, and multiple game screens.

> **Note:** This project was originally developed in Grade 11 and is being shared as one of my early programming projects. The code reflects my experience at the time.

---

## Features

- Poker hand evaluation
- Multiple Joker cards with unique abilities
- Score and multiplier calculations
- Interactive card selection
- Animated game screens
- Main menu and game UI
- Mouse-based controls
- Win/Loss conditions
- Deck and hand management

---

## Technologies Used

- Python 3
- Pygame Zero
- pgzhelper

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/balatro-clone.git
cd balatro-clone
```

### 2. Install Python

Download Python (3.11 or newer recommended):

https://www.python.org/downloads/

During installation, make sure **"Add Python to PATH"** is checked.

---

### 3. Install required packages

Open Command Prompt or Terminal and run:

```bash
pip install pgzero
pip install pgzhelper
```

If `pip` doesn't work, try:

```bash
python -m pip install pgzero
python -m pip install pgzhelper
```

or

```bash
py -m pip install pgzero
py -m pip install pgzhelper
```

---

## Running the Game

Navigate to the project folder and run:

```bash
pgzrun main.py
```

If your main file has a different name, replace `main.py` with the correct filename.

Example:

```bash
pgzrun game.py
```

---

## Controls

- **Mouse** – Select and play cards
- Use the on-screen buttons to navigate menus and gameplay.

---

## Project Structure

```
assets/          # Images, sounds, fonts
main.py          # Main game entry point
cards.py         # Card logic
jokers.py        # Joker abilities
...
```

*(Your file names may differ.)*

---

## What I Learned

While building this project, I gained experience with:

- Object-Oriented Programming
- Event-driven programming
- Game state management
- Poker hand detection algorithms
- Score calculation systems
- Working with external Python libraries
- GUI development
- Debugging larger Python projects

---

## Future Improvements

Some improvements I'd like to make include:

- Cleaner code structure
- Better documentation
- Improved animations
- Additional Joker abilities
- Addition of Planet and Tarot cards
- More polished UI
- Saving/loading game progress
- Refactoring repeated code

---

## Disclaimer

Balatro is an original game created by LocalThunk. This project is an educational recreation made for learning purposes and is **not intended for commercial use**.

---

## Author

Kalvin Lee
