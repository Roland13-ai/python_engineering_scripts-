# Engineering Scripts & Notebooks

![Status](https://img.shields.io/badge/status-active-brightgreen)

![License](https://img.shields.io/badge/license-MIT-blue)
## Overview
A collection of Python scripts and Jupyter notebooks covering engineering foundations, scientific calculations, applied projects, and Arduino-related tools.

## About
- **Purpose:** Centralize the code I write while learning and applying electrical/electronics engineering concepts.
- **Why I built it:** To keep my calculations, simulations, and small tools organized in one place instead of scattered files.

## Repository Structure

### `01_foundations/`
Python & NumPy fundamentals applied to circuit theory — from array operations to a reusable impedance-calculation module (`circuits.py`), tested and applied to Kirchhoff's law and voltage dividers.

### `02_Scientific_Calculation/`
Advanced scientific computing — symbolic circuit analysis (SymPy), differential equation solving (SciPy), signal filtering (Butterworth), and frequency response modeling, including a Python/Octave syntax comparison.

### `03_projects/`
Applied mini-projects built on the foundations above. See [`03_projects/README.md`](./03_projects/README.md) for details — currently featuring a complete series RLC circuit analysis tool (NumPy + SymPy + Matplotlib + CSV export).

### `04_Arduino/`
Python/Arduino-adjacent hardware exercises. See [`04_Arduino/NOTES.md`](./04_Arduino/NOTES.md) — currently featuring Bluetooth-controlled LEDs (HC-05) with Proteus wiring simulation.

## Tech Stack
`Python` `NumPy` `SciPy` `SymPy` `Matplotlib` `Jupyter Notebook` `Arduino (C++)`

## Installation
1. Clone the repo
   ```bash
   git clone https://github.com/Roland13-ai/python-engineering-scripts.git
2. Install dependencies
numpy scipy sympy matplotlib
3. Run any script or open a notebook with Jupyter
Notes
This repo evolves as I learn — folders will grow as new topics and projects are added.
