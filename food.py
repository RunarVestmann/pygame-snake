
import pygame
import random
from constants import CELL_SIZE

class Food:
    def __init__(self, _x=0, _y=0):
        self.x = _x
        self.y = _y

    def render(self, screen): 
        pygame.draw.rect(screen, "red", pygame.Rect(self.x, self.y, CELL_SIZE, CELL_SIZE))

    def respawn(self, screen, snake): 
        available = [] 
        for x in range(0, screen.get_width(), CELL_SIZE):
            for y in range(0, screen.get_height(), CELL_SIZE):
                is_free = True
                if snake.x == x and snake.y == y:
                    is_free = False
                for segment in snake.segments:
                    if segment.x == x and segment.y == y:
                        is_free = False

                if is_free:
                    available.append((x, y))

        cell = available[random.randint(0, len(available) - 1)]
        self.x = cell[0]
        self.y = cell[1]