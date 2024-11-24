import pygame
from Configs import WIDTH, HEIGHT, CELL_SIZE, ROWS, COLS, RED, GRAY, WHITE, GREEN, AMARELO

class Cell:
    def __init__(self, row, col, is_wall):
        self.row = row
        self.col = col
        self.x = row * CELL_SIZE
        self.y = col * CELL_SIZE
        self.color = GRAY if is_wall else WHITE
        self.visited = False
        self.is_wall = is_wall

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.y, self.x, CELL_SIZE, CELL_SIZE))

    def make_start(self):
        self.color = GREEN

    def make_end(self):
        self.color = RED

    def make_visited(self):
        if not self.is_wall:
            self.color = AMARELO

    def toggle_wall(self):
        """Alterna o estado da célula entre parede e caminho."""
        self.is_wall = not self.is_wall
        self.color = GRAY if self.is_wall else WHITE