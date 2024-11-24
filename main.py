import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from food import Food
from snake import Snake

def game_loop():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    snake = Snake()
    food = Food()

    direction = "RIGHT"
    new_direction = "RIGHT"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and direction != "DOWN":
                    new_direction = "UP"
                if event.key == pygame.K_s and direction != "UP":
                    new_direction = "DOWN"
                if event.key == pygame.K_a and direction != "RIGHT":
                    new_direction = "LEFT"
                if event.key == pygame.K_d and direction != "LEFT":
                    new_direction = "RIGHT"

        direction = new_direction
        snake.move(direction, screen)

        if snake.x == food.x and snake.y == food.y:
            food.respawn(screen, snake)
            snake.grow()

        if snake.is_colliding_with_self():
            return

        screen.fill("black")

        food.render(screen)
        snake.render(screen)

        pygame.display.flip()
        clock.tick(4)  

def main():
    pygame.init()
    game_loop()
    pygame.quit()

main()