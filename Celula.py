import pygame
from Configs import CELL_SIZE, RED, GRAY, WHITE, GREEN, YELLOW

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
            self.color = YELLOW