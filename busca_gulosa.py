import pygame
import time
from mapa import maze
from celula import Cell
from queue import PriorityQueue
from utils import make_grid, draw_grid, get_neighbors
from configs import  font, win

pygame.display.set_caption("Busca Gulosa com Heurística de Chebyshev")

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
        draw_grid(win, grid, steps, font)
        time.sleep(0.15)

        neighbors = get_neighbors(grid, current)
        for neighbor in neighbors:
            if not neighbor.visited and not neighbor.is_wall:
                neighbor.visited = True
                priority = chebyshev_distance(neighbor, end)
                pq.put(PriorityItem(priority, neighbor))  # Adiciona na fila com a prioridade calculada

    return steps  # Retorna o total de passos percorridos

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
                    steps = greedy_chebyshev(grid, start, end)  # Executa a busca e armazena o número de passos

        pygame.display.update()

    pygame.quit()

main(win)
