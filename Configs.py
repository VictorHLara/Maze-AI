import pygame

# Configurações da grade
WIDTH, HEIGHT = 600, 600  # Tamanho da tela
ROWS, COLS = 12, 12  # Tamanho do labirinto (12x12)
CELL_SIZE = WIDTH // COLS  # Tamanho de cada célula

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
AMARELO = (255, 255, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (46, 46, 46)  # Cor das paredes