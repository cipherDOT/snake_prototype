import pygame
import random
from pygame.math import Vector2

pygame.font.init()

FONT = pygame.font.SysFont('comicsans', 50)

cell_num = 20
cell_size = 40
score = 0

display = pygame.display.set_mode((cell_num * cell_size, cell_num * cell_size))
pygame.display.set_caption('Snake')

# ------------------------------------------------------------------------------------------------------------------------- #


class Fruit(object):
    def __init__(self):
        self.randomize()

    def draw(self):
        fruit_rect = pygame.Rect(
            int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        pygame.draw.rect(display, (255, 70, 70), fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_num - 1)
        self.y = random.randint(0, cell_num - 1)
        self.pos = Vector2(self.x, self.y)

# ------------------------------------------------------------------------------------------------------------------------- #


class Snake(object):
    def __init__(self):
        self.body = [Vector2(7, 10), Vector2(8, 10), Vector2(9, 10)]
        self.direction = Vector2(-1, 0)
        self.new_block = False

    def draw(self):
        for block in self.body:
            block_rect = pygame.Rect(
                int(block.x * cell_size), int(block.y * cell_size), cell_size, cell_size)
            pygame.draw.rect(display, (169, 169, 169), block_rect)

    def move(self):
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy

    def add_block(self):
        self.new_block = True

# ------------------------------------------------------------------------------------------------------------------------- #


class Main(object):

    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        self.snake.move()
        self.collide()
        self.end()

    def draw(self):
        self.snake.draw()
        self.fruit.draw()

    def collide(self):
        global score
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            score += 1

    def end(self):
        if not 0 <= self.snake.body[0].x < cell_num or not 0 <= self.snake.body[0].y < cell_num:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        quit()

# ------------------------------------------------------------------------------------------------------------------------- #


def draw_grid(display):
    for i in range(1, cell_num):
        for j in range(1, cell_num):
            pygame.draw.line(display, (255, 255, 255), (i * cell_size,
                                                        0), (i * cell_size, cell_size * cell_num))
            pygame.draw.line(display, (255, 255, 255), (0, j *
                                                        cell_size), (cell_size * cell_num, j * cell_size))

# ------------------------------------------------------------------------------------------------------------------------- #


def main():
    run = True
    game = Main()

    clock = pygame.time.Clock()
    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 150)

    while run:
        display.fill((51, 51, 51))
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == SCREEN_UPDATE:
                game.update()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and game.snake.direction != (0, 1):
                    game.snake.direction = Vector2(0, -1)
                elif event.key == pygame.K_DOWN and game.snake.direction != (0, -1):
                    game.snake.direction = Vector2(0, 1)
                elif event.key == pygame.K_RIGHT and game.snake.direction != (-1, 0):
                    game.snake.direction = Vector2(1, 0)
                elif event.key == pygame.K_LEFT and game.snake.direction != (1, 0):
                    game.snake.direction = Vector2(-1, 0)

        game.draw()
        score_text = FONT.render('Score: ' + str(score), 1, (255, 255, 255))
        display.blit(score_text, (10, 10))
        # snake.move()
        draw_grid(display=display)

        pygame.display.flip()


if __name__ == '__main__':
    main()
