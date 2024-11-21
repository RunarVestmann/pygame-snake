import pygame
import random

CELL_SIZE = 40

class Snake:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.segments = []

    def render(self, screen):
        pygame.draw.rect(screen, "green", pygame.Rect(self.x, self.y, CELL_SIZE, CELL_SIZE))
        for segment in self.segments:
            pygame.draw.rect(screen, (0, 127, 0), pygame.Rect(segment.x, segment.y, CELL_SIZE, CELL_SIZE))

class SnakeSegment:
    def __init__(self):
        self.x = -100
        self.y = -100

class Food:
    def __init__(self):
        self.x = 0
        self.y = 0

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    snake = Snake()
    food = Food()

    direction = "RIGHT"

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and direction != "DOWN":
                    direction = "UP"
                if event.key == pygame.K_s and direction != "UP":
                    direction = "DOWN"
                if event.key == pygame.K_a and direction != "RIGHT":
                    direction = "LEFT"
                if event.key == pygame.K_d and direction != "LEFT":
                    direction = "RIGHT"

        if len(snake.segments) > 0:
            tail = snake.segments.pop()
            tail.x = snake.x
            tail.y = snake.y
            snake.segments.insert(0, tail)

        if direction == "DOWN":
            snake.y += CELL_SIZE
        if direction == "UP":
            snake.y -= CELL_SIZE
        if direction == "LEFT":
            snake.x -= CELL_SIZE
        if direction == "RIGHT":
            snake.x += CELL_SIZE

        if snake.x == food.x and snake.y == food.y:
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
            food.x = cell[0]
            food.y = cell[1]
            snake.segments.append(SnakeSegment())

        for segment in snake.segments:
            if snake.x == segment.x and snake.y == segment.y:
                running = False
                return

        if snake.x < 0:
            snake.x = screen.get_width() - CELL_SIZE
        if snake.y < 0:
            snake.y = screen.get_height() - CELL_SIZE

        if snake.x >= screen.get_width():
            snake.x = 0
        if snake.y >= screen.get_height():
            snake.y = 0

        screen.fill("black")

        pygame.draw.rect(screen, "red", pygame.Rect(food.x, food.y, CELL_SIZE, CELL_SIZE))

        snake.render(screen)

        pygame.display.flip()

        clock.tick(4)  

    pygame.quit()



main()