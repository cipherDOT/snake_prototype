import pygame
from pygame.math import Vector2
import time
import random

pygame.font.init()

width = 600
height = 600
rez = 30
black = (0, 0, 0)
white = (255, 255, 255)
framerate = 10

display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake')

font = pygame.font.SysFont("comicsans", 25)

# -------------------------------------------------------------------------------------------------------------------------#


class Snake(object):

    def __init__(self):
        self.body = [Vector2(7, 10), Vector2(6, 10), Vector2(5, 10)]
        # self.body = [Vector2(0, 0)]
        self.dirn = Vector2(0, -1)
        self.head = self.body[0]

    def draw(self):
        for cell in self.body:
            pygame.draw.rect(display, (169, 169, 169), (int(
                cell.x) * rez, int(cell.y) * rez, rez, rez))

    def move(self):
        nextx = self.body[0].x
        nexty = self.body[0].y
        self.body[0] += self.dirn
        for cell in self.body[1:]:
            # if self.body.index(cell) == 0:
            #     pass
            # else:
            thisx = cell.x
            thisy = cell.y
            cell.x = nextx
            cell.y = nexty
            nextx = thisx
            nexty = thisy

    def grow(self):
        self.body.append(Vector2(self.body[-1:][0].x, self.body[-1:][0].y))

    def end(self):
        if self.head in self.body[1:]:
            return True

        if self.head.x * rez > width or self.head.x < 0 or self.head.y * rez > height or self.head.y < 0:
            return True

    def set_dirn(self, x, y):
        self.dirn = Vector2(x, y)

# -------------------------------------------------------------------------------------------------------------------------#


class Food(object):
    def __init__(self):
        self.x = random.randint(0, width - rez)
        self.y = random.randint(0, height - rez)
        self.pos = Vector2(self.x - (self.x % rez), self.y - (self.y % rez))

    def draw(self):
        pygame.draw.rect(display, (255, 0, 70),
                         (int(self.pos.x), int(self.pos.y), rez, rez))

    def pick_new(self):
        self.x = random.randint(0, width - rez)
        self.y = random.randint(0, height - rez)
        self.pos = Vector2(self.x - (self.x % rez), self.y - (self.y % rez))


# -------------------------------------------------------------------------------------------------------------------------#


def draw_grid():
    for i in range(1, width // rez):
        for j in range(1, height // rez):
            pygame.draw.line(display, (255, 255, 255),
                             (i * rez, 0), (i * rez, height))
            pygame.draw.line(display, (255, 255, 255),
                             (0, j * rez), (width, j * rez))

# -------------------------------------------------------------------------------------------------------------------------#


def main():
    run = True
    snake = Snake()
    food = Food()
    score = 0
    counter = 0
    clock = pygame.time.Clock()

    while run:
        clock.tick(framerate)
        display.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.dirn.y != 1:
                    snake.set_dirn(0, -1)
                elif event.key == pygame.K_DOWN and snake.dirn.y != -1:
                    snake.set_dirn(0, 1)
                elif event.key == pygame.K_LEFT and snake.dirn.x != 1:
                    snake.set_dirn(-1, 0)
                elif event.key == pygame.K_RIGHT and snake.dirn.x != -1:
                    snake.set_dirn(1, 0)

        if (snake.head.x*rez == food.pos.x and snake.head.y*rez == food.pos.y):
            food.pick_new()
            snake.grow()
            score += 1

        if snake.end():
            lost_text = font.render('You Lost!', 3, (255, 255, 255))
            display.blit(lost_text, ((width // 2) - (lost_text.get_width() //
                                                     2), (height // 2) - (lost_text.get_height() // 2)))
            counter += 1

        if counter > 0:
            time.sleep(2)
            run = False

        snake.move()
        food.draw()
        snake.draw()
        score_text = font.render(str(score), 1, (255, 255, 255))
        display.blit(score_text, (10, 10))
        draw_grid()

        pygame.display.flip()


# -------------------------------------------------------------------------------------------------------------------------#


if __name__ == "__main__":
    main()

# -------------------------------------------------------------------------------------------------------------------------#
