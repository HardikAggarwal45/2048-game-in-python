# 2048-Tkinter-Python

A lightweight, logic-driven implementation of the classic 2048 game using Python's Tkinter library.

## 📝 Project Overview
This project is a desktop application that clones the popular 2048 puzzle mechanics. It focuses on clean GUI design and robust state management. Built as a deep dive into 2D matrix manipulation and event-driven programming.

## ✨ Key Features
* **Intuitive Controls:** Full support for keyboard arrow keys.
* **Smart Spawning:** New tiles (2s or 4s) only spawn when a move successfully changes the board state.
* **Visual Grid:** A polished UI featuring a custom color palette, tile padding, and a "tray" effect for the game board.
* **Win/Loss Detection:** Automatic detection of the 2048 victory condition and "No Moves Left" game-over state.
* **Restart Functionality:** Instant board reset via a dedicated UI button.

## 🛠️ Technical Implementation
* **Matrix Logic:** Uses **Matrix Transposition** and **Row Reversal** to handle all 4 directions of movement through a single centralized `execute()` core.
* **State Management:** Implemented manual deep-copying of the game board to track changes between moves accurately.
* **GUI Architecture:** Utilizes the `Tkinter.Label` grid system with dynamic configuration for background and foreground colors.

## 🚀 Getting Started

### Prerequisites
* Python 3.x
* Tkinter (usually included with standard Python installations)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/HardikAggarwal45/2048-Tkinter-Python.git
   ```

2. Navigate to the directory:
   ```bash
   cd 2048-Tkinter-Python
   ```

3. Run the game:
   ```bash
   python main.py
   ```

## 🎮 How to Play
* **Arrow Keys:** Slide tiles in the desired direction.
* **Merge:** Tiles with the same value merge into one when they collide.
* **Goal:** Reach the **2048** tile!

## 🔭 Future Scope
* [ ] Add a Score and High-Score counter.
* [ ] Implement an "Undo" move feature.
* [ ] Add a Minimax-based AI solver.

---
Developed by **Hardik Aggarwal**