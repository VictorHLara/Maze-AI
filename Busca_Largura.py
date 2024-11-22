import time
from collections import deque
from Mapa import maze
from Celula import Cell
from Configs import WIDTH, HEIGHT, CELL_SIZE, ROWS, COLS, RED, GRAY, WHITE, GREEN, AMARELO
import pygame

# Inicializa o pygame
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Busca em Largura")

# Fonte para exibir o número de passos
font = pygame.font.SysFont(None, 36)

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

# Algoritmo BFS com verificação de paredes e contagem de passos
def bfs(grid, start, end):
    queue = deque([start])
    start.visited = True
    steps = 0  # Contador de passos

    while queue:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = queue.popleft()
        steps += 1  # Incrementa o contador de passos a cada nova célula visitada

        if current == end:
            return steps  # Retorna o total de passos ao final da busca

        current.make_visited()
        draw_grid(win, grid, steps)
        time.sleep(0.15)

        neighbors = get_neighbors(grid, current)
        for neighbor in neighbors:
            if not neighbor.visited and not neighbor.is_wall:
                neighbor.visited = True
                queue.append(neighbor)

    return steps  # Caso não encontre, retorna o total de passos percorridos

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
    steps = None  # Variável para armazenar o total de passos

    while running:
        draw_grid(win, grid, steps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started:
                    started = True
                    steps = bfs(grid, start, end)  # Executa a busca e armazena o número de passos

        pygame.display.update()

    pygame.quit()

main(win)
