import pygame
from Celula import Cell
from Configs import ROWS, COLS, WHITE

def make_grid(maze, Cell):
    """Cria a grade a partir do labirinto."""
    return [[Cell(i, j, maze[i][j] == 0) for j in range(COLS)] for i in range(ROWS)]

def draw_grid(win, grid, steps=None, font=None):
    """Desenha a grade e exibe o número de passos."""
    win.fill(WHITE)
    for row in grid:
        for cell in row:
            cell.draw(win)
    if steps is not None and font is not None:
        steps_text = font.render(f"Passos: {steps}", True, WHITE)
        win.blit(steps_text, (10, 10))
    pygame.display.update()

def get_neighbors(grid, cell, rows=ROWS, cols=COLS):
    """Retorna os vizinhos válidos de uma célula."""
    neighbors = []
    if cell.row > 0:  # Cima
        neighbors.append(grid[cell.row - 1][cell.col])
    if cell.col > 0:  # Esquerda
        neighbors.append(grid[cell.row][cell.col - 1])
    if cell.col < cols - 1:  # Direita
        neighbors.append(grid[cell.row][cell.col + 1])
    if cell.row < rows - 1:  # Baixo
        neighbors.append(grid[cell.row + 1][cell.col])
    return neighbors
