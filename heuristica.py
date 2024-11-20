import pygame
import time
from queue import PriorityQueue

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
pygame.display.set_caption("Busca Gulosa com Heurística de Chebyshev")

# Fonte para exibir o número de passos
font = pygame.font.SysFont(None, 36)

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

# Classe para encapsular itens na fila de prioridades
class PriorityItem:
    def __init__(self, priority, cell):
        self.priority = priority
        self.cell = cell

    def __lt__(self, other):
        return self.priority < other.priority

# Função de distância Chebyshev
def chebyshev_distance(cell1, cell2):
    return max(abs(cell1.row - cell2.row), abs(cell1.col - cell2.col))

# Algoritmo de busca gulosa com heurística de Chebyshev
def greedy_chebyshev(grid, start, end):
    pq = PriorityQueue()
    pq.put(PriorityItem(0, start))  # Adiciona o item inicial na fila com prioridade 0
    steps = 0  # Contador de passos

    while not pq.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current_item = pq.get()  # Recupera o item com a menor prioridade
        current = current_item.cell
        steps += 1

        if current == end:
            return steps  # Retorna o total de passos ao encontrar o objetivo

        current.make_visited()
        draw_grid(win, grid, steps)
        time.sleep(0.15)

        neighbors = get_neighbors(grid, current)
        for neighbor in neighbors:
            if not neighbor.visited and not neighbor.is_wall:
                neighbor.visited = True
                priority = chebyshev_distance(neighbor, end)
                pq.put(PriorityItem(priority, neighbor))  # Adiciona na fila com a prioridade calculada

    return steps  # Retorna o total de passos percorridos

# Função para obter vizinhos de uma célula
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

# Criação da grade a partir do labirinto
def make_grid(maze):
    return [[Cell(i, j, maze[i][j] == 0) for j in range(COLS)] for i in range(ROWS)]

# Desenha a grade e o número de passos na tela
def draw_grid(win, grid, steps=None):
    win.fill(WHITE)
    for row in grid:
        for cell in row:
            cell.draw(win)
    if steps is not None:
        steps_text = font.render(f"Passos: {steps}", True, WHITE)
        win.blit(steps_text, (10, 10))
    pygame.display.update()

# Função principal
def main(win):
    grid = make_grid(maze)
    start = grid[4][11]  # Ponto inicial
    end = grid[10][0]  # Ponto final
    start.make_start()
    end.make_end()

    running = True
    started = False
    steps = None  # Variável para armazenar o total de passos

    while running:
        draw_grid(win, grid, steps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started:
                    started = True
                    steps = greedy_chebyshev(grid, start, end)  # Executa a busca e armazena o número de passos

        pygame.display.update()

    pygame.quit()

main(win)
