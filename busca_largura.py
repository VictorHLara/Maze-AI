import time
from collections import deque
from mapa import maze
from celula import Cell
from configs import font, win
from utils import make_grid, draw_grid, get_neighbors
import pygame

pygame.display.set_caption("Busca em Largura")

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
        draw_grid(win, grid, steps, font)
        time.sleep(0.15)

        neighbors = get_neighbors(grid, current)
        for neighbor in neighbors:
            if not neighbor.visited and not neighbor.is_wall:
                neighbor.visited = True
                queue.append(neighbor)

    return steps  # Caso não encontre, retorna o total de passos percorridos

# Função principal
def main(win):
    grid = make_grid(maze, Cell)
    start = grid[4][11]  # Ponto inicial
    end = grid[10][0]  # Ponto final
    start.make_start()
    end.make_end()

    running = True
    started = False
    steps = None  # Variável para armazenar o total de passos

    while running:
        draw_grid(win, grid, steps,font)
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
