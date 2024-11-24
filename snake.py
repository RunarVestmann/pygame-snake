
import pygame
from constants import CELL_SIZE, SNAKE_HEAD_COLOR, SNAKE_SEGMENT_COLOR

class Snake:
    class SnakeSegment:
        def __init__(self):
            self.x = -100
            self.y = -100

    def __init__(self):
        self.x = 0
        self.y = 0
        self.segments = []

    def render(self, screen):
        pygame.draw.rect(screen, SNAKE_HEAD_COLOR, pygame.Rect(self.x, self.y, CELL_SIZE, CELL_SIZE))
        for segment in self.segments:
            pygame.draw.rect(screen, SNAKE_SEGMENT_COLOR, pygame.Rect(segment.x, segment.y, CELL_SIZE, CELL_SIZE))

    def grow(self): 
        self.segments.append(self.SnakeSegment())

    def is_colliding_with_self(self): 
        for segment in self.segments:
            if self.x == segment.x and self.y == segment.y:
                return True
        return False
    
    def __wrap_around(self, screen):
        if self.x < 0:
            self.x = screen.get_width() - CELL_SIZE
        if self.y < 0:
            self.y = screen.get_height() - CELL_SIZE

        if self.x >= screen.get_width():
            self.x = 0
        if self.y >= screen.get_height():
            self.y = 0

    def move(self, direction, screen):
        if len(self.segments) > 0:
            tail = self.segments.pop()
            tail.x = self.x
            tail.y = self.y
            self.segments.insert(0, tail)

        if direction == "DOWN":
            self.y += CELL_SIZE
        if direction == "UP":
            self.y -= CELL_SIZE
        if direction == "LEFT":
            self.x -= CELL_SIZE
        if direction == "RIGHT":
            self.x += CELL_SIZE

        self.__wrap_around(screen)