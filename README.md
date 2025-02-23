# 🧠 Search Agents Visualization

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pygame](https://img.shields.io/badge/-Pygame-ffa500?logo=python&logoColor=white&style=for-the-badge)

A Python pathfinding visualization tool using Pygame that demonstrates the Greedy Best-First Search algorithm with the Chebyshev distance heuristic, Depth-first search (DFS) and Breadth-first search (BFS). This project provides an interactive way to explore how the algorithm navigates through a predefined maze grid.

## 👾 Features

- **Grid Visualization**: Displays a 2D maze grid with start (green) and end (red) points, walls (black), and visited nodes (yellow).
- **Step-by-Step Animation**: Visualizes the algorithm's exploration process in real-time with a 0.15-second delay between steps.
- **Chebyshev Distance Heuristic**: Uses the formula `max(|x₁ - x₂|, |y₁ - y₂|)` to prioritize node exploration ( for Greedy Search).
- **Priority Queue Management**: Efficiently selects the next node using a priority queue based on heuristic values ( for Greedy Search).
- **Step Counter**: Tracks and displays the total steps taken during the search.
- **Stochastic environment**: 25% chance of noise in the search.  

 ## 📚 Dependencies

- Python 3.x
- Pygame

 ## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/VictorHLara/Maze-AI.git
   cd Maze-AI
   ```
2. Install dependencies:
   ```bash
   pip install pygame
   ```
## 🕹️ Usage

  - Start Search: Press the `SPACE` to begin the algorithm.

  - Exit: Close the window or press `ESC`.

## ⚙️ Customization

1. Modify the Maze:
   - Edit the maze list in mapa.py (0 = walkable, 1 = wall).
2. Change Start/End Positions
   - Update the coordinates in main.py.
  
## 🎯 Preview
  - Finished Greedy Search with no noise.

![Image](https://github.com/user-attachments/assets/4c7b8302-5cb7-4264-81db-e1201add3a0e)



   
  
   
   
