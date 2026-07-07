# Balatro Clone (Python)

A recreation of the popular roguelike poker game **Balatro**, developed in **Grade 11** using **Python**, **Pygame Zero**, and **pgzhelper**.

This project was created to practice game development, object-oriented programming, event-driven programming, and complex game logic. It includes a complete poker-based scoring system, custom Joker mechanics, animated gameplay, shop progression, boss encounters, and multiple game states.

> **Note:** This project was originally developed in Grade 11 and is being shared as one of my early programming projects. The code reflects my experience at the time, but demonstrates my ability to build a complete game system from scratch.

---

## Features

### Poker Gameplay System

- Full poker hand evaluation system
- Supports:
  - Royal Flush
  - Straight Flush
  - Four of a Kind
  - Full House
  - Flush
  - Straight
  - Three of a Kind
  - Two Pair
  - Pair
  - High Card
- Custom Ace-low straight detection
- Dynamic hand scoring

---

### Scoring System

- Separate chip and multiplier calculations inspired by roguelike deckbuilders
- Calculates final score using:

```
Chips × Multiplier
```

- Tracks:
  - Current score
  - Best hand score
  - Hands played
  - Cards used
  - Cards discarded

---

### Joker System

Implemented a modular Joker system with unique gameplay effects.

Includes:

- Joker purchasing system
- Joker selling system
- Joker descriptions and hover information
- Joker selection animations
- Multiple Joker categories:
  - Score modifiers
  - Suit-based effects
  - Rank-based effects
  - Economy bonuses
  - Multiplier effects
  - Card manipulation effects

Examples of implemented Joker mechanics:

- Increasing chips or multipliers
- Triggering effects based on suits
- Triggering effects based on card ranks
- Modifying scoring conditions
- Providing money rewards

---

### Roguelike Progression

Complete game loop including:

- Multiple antes
- Small blinds
- Big blinds
- Boss blinds
- Shop phase
- Final win/loss screens

Gameplay flow:

```
Start Game
    ↓
Play Blind
    ↓
Earn Money
    ↓
Visit Shop
    ↓
Upgrade Deck
    ↓
Advance Ante
    ↓
Defeat Final Boss
```

---

### Boss Blind System

Includes custom boss mechanics that modify gameplay:

- Suit restrictions
- Face card restrictions
- Special gameplay rules
- Unique blind conditions

Boss effects are checked during scoring and card selection.

---

### Card Management

Implemented:

- Random card generation
- Card selection system
- Card movement animations
- Card deletion after playing/discarding
- Hand organization
- Deck tracking
- Used card tracking

---

### User Interface

Created multiple custom game screens:

- Main menu
- Game screen
- Shop screen
- Joker collection screen
- Information screen
- Hand information screen
- Win/Loss statistics screen

Includes:

- Animated cards
- Hover descriptions
- Interactive buttons
- Pixel-style UI
- Mouse-based controls

---

### Statistics Tracking

The game records:

- Jokers purchased
- Jokers sold
- Cards played
- Cards discarded
- Best hand
- Most played hand
- Hands completed
- Round progression

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

---

### 2. Install Python

Download Python (3.11 or newer recommended):

https://www.python.org/downloads/

During installation, make sure:

```
Add Python to PATH
```

is enabled.

---

### 3. Install required packages

Open Command Prompt or Terminal and run:

```bash
pip install pgzero
pip install pgzhelper
```

If `pip` does not work:

```bash
python -m pip install pgzero
python -m pip install pgzhelper
```

or:

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
pgzrun balatro.py
```

---

## Controls

### Mouse Controls

- Click cards to select/deselect them
- Click **PLAY** to play a hand
- Click **DISCARD** to discard selected cards
- Click Jokers to buy, sell, or view information
- Navigate menus using buttons

---

## Project Structure

```
Balatro/
│
├── images/              # Game sprites and UI assets
├── fonts/               # Pixel font files
├── music/               # Audio files
│
├── main.py              # Main game logic and entry point
├── jokers.txt           # Joker data
├── blinds.txt           # Blind data
│
└── README.md
```

---

## Code Structure

### Card System

Responsible for:

- Generating cards
- Tracking cards in the deck
- Handling card selection
- Managing card movement

### Hand Evaluation System

Responsible for:

- Detecting poker hands
- Determining hand strength
- Assigning base chip and multiplier values

### Joker Engine

Responsible for:

- Applying Joker effects
- Managing Joker inventory
- Handling Joker triggers

### Game State System

Handles transitions between:

- Menu
- Gameplay
- Shop
- Victory
- Defeat

---

## What I Learned

While building this project, I gained experience with:

- Game development in Python
- Object-oriented programming concepts
- Event-driven programming
- Managing large-scale game logic
- Creating poker hand evaluation algorithms
- Implementing scoring systems
- Designing modular game mechanics
- Creating GUI systems
- Handling animations and user input
- Debugging complex projects

---

## Future Improvements

Some improvements I would like to make include:

- Refactoring repeated code into reusable functions
- Separating systems into multiple Python files
- Adding more documentation
- Improving object-oriented design
- Adding save/load functionality
- Adding additional card types
- Adding Planet and Tarot card systems
- Improving animations
- Expanding Joker variety
- Creating a more polished user interface

---

## Disclaimer

Balatro is an original game created by LocalThunk.

This project is an educational recreation made for programming practice and learning purposes. It is not intended for commercial use.

---

## Author

Kalvin Lee
