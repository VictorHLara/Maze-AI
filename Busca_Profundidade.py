import pygame
import time
from Celula import Cell
from Configs import WIDTH, HEIGHT, CELL_SIZE, ROWS, COLS, RED, GRAY, WHITE, GREEN, AMARELO, win, font
from Mapa import maze
from Utils import make_grid, draw_grid, get_neighbors

pygame.display.set_caption("Busca em Profundidade")

# Algoritmo DFS com verificação de paredes e contagem de passos
def dfs(grid, start, end):
    stack = [start]
    steps = 0  # Contador de passos

    while stack:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = stack.pop()
        steps += 1  # Incrementa o contador de passos a cada nova célula visitada

        if current == end:
            return steps  # Retorna o total de passos ao final da busca

        current.make_visited()
        draw_grid(win, grid, steps, font)
        time.sleep(0.08)

        # Obtém os vizinhos na ordem especificada e adiciona na pilha na ordem inversa
        neighbors = get_neighbors(grid, current)
        for neighbor in reversed(neighbors):
            if not neighbor.visited and not neighbor.is_wall:
                neighbor.visited = True
                stack.append(neighbor)

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
        draw_grid(win, grid, steps, font)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started:
                    started = True
                    steps = dfs(grid, start, end)  # Executa a busca e armazena o número de passos

        pygame.display.update()

    pygame.quit()

main(win)
