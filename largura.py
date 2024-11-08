import pygame
import time
from collections import deque

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

# Inicializa o pygame
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Busca em Largura (BFS) - Labirinto com Pygame")

# Labirinto 12x12 (1 = caminho, 0 = parede)
maze = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1],
    [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


# Classe para representar cada célula na grade
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

# Criação da grade a partir do labirinto
def make_grid(maze):
    return [[Cell(i, j, maze[i][j] == 0) for j in range(COLS)] for i in range(ROWS)]

# Desenha a grade na tela
def draw_grid(win, grid):
    win.fill(WHITE)
    for row in grid:
        for cell in row:
            cell.draw(win)
    pygame.display.update()

# Algoritmo BFS com verificação de paredes
def bfs(grid, start, end):
    queue = deque([start])
    start.visited = True

    while queue:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = queue.popleft()
        if current == end:
            return True

        current.make_visited()
        draw_grid(win, grid)
        time.sleep(0.15)

        neighbors = get_neighbors(grid, current)
        for neighbor in neighbors:
            if not neighbor.visited and not neighbor.is_wall:
                neighbor.visited = True
                queue.append(neighbor)

    return False

# Função para obter vizinhos de uma célula na ordem: ↑, ←, →, ↓
def get_neighbors(grid, cell):
    neighbors = []
    if cell.row > 0:  # Cima
        neighbors.append(grid[cell.row - 1][cell.col])
    if cell.col > 0:  # Esquerda
        neighbors.append(grid[cell.row][cell.col - 1])
    if cell.col < COLS - 1:  # Direita
        neighbors.append(grid[cell.row][cell.col + 1])
    if cell.row < ROWS - 1:  # Baixo
        neighbors.append(grid[cell.row + 1][cell.col])
    return neighbors

# Função principal
def main(win):
    grid = make_grid(maze)
    start = grid[4][11]  # Ponto inicial
    end = grid[10][0]  # Ponto final
    start.make_start()
    end.make_end()

    running = True
    started = False

    while running:
        draw_grid(win, grid)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started:
                    started = True
                    bfs(grid, start, end)
        pygame.display.update()

    pygame.quit()

main(win)
