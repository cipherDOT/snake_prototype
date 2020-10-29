
# ------------------------------------------------------------------------------------------------------------------------- #
import pygame
import random

pygame.font.init()

font = pygame.font.SysFont('comicsans', 40)

width = 600
height = 400
rez = 20

display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake')

# ------------------------------------------------------------------------------------------------------------------------- #

class Snake:
    color = (255, 255, 255)
    body = []


    def __init__(self, x, y):
        self.x = x
        self.y = y
        
# ------------------------------------------------------------------------------------------------------------------------- #
class Cell:
    color = (255, 255, 255)

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dirn = 'up'


    def move_up(self, rez):
        self.y -= rez

    def move_down(self, rez):
        self.y += rez

    def move_left(self, rez):
        self.x -= rez

    def move_right(self, rez):
        self.x += rez

# ------------------------------------------------------------------------------------------------------------------------- #
class Food:
    color = (255, 40, 70)

    def __init__(self):
        self.eaten = False
        self.x = random.randint(20, width - 40)
        self.y = random.randint(20, height - 40)

    def change_pos(self):
        self.eaten = False
        self.x = random.randint(20, width - 40)
        self.y = random.randint(20, height - 40)

# ------------------------------------------------------------------------------------------------------------------------- #
def main():
    run = True
    cell = Cell(100, 100)
    pi = Food()
    score = 0

    clock = pygame.time.Clock()

    while run:
        clock.tick(15)

        display.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            cell.y -= rez
            cell.dirn = 'up'

        elif keys[pygame.K_DOWN]:
            cell.y += rez
            cell.dirn = 'down'

        elif keys[pygame.K_LEFT]:
            cell.x -= rez
            cell.dirn = 'left'

        elif keys[pygame.K_RIGHT]:
            cell.x += rez
            cell.dirn = 'right'

        for i in range(1, width // rez):
            pygame.draw.line(display, (169, 169, 169), (i*rez, 0), (i*rez, height))

        for j in range(1, height // rez):
            pygame.draw.line(display, (169, 169, 169), (0,  j*rez), (width, j*rez))

        if cell.dirn == 'up':
            cell.y -= rez
        elif cell.dirn == 'down':
            cell.y += rez
        elif cell.dirn == 'left':
            cell.x -= rez
        elif cell.dirn == 'right':
            cell.x += rez

        if (cell.x == pi.x - (pi.x % rez) and cell.y == pi.y - (pi.y % rez)):
            score += 1
            pi.eaten = True
            pi.change_pos()

        if not pi.eaten:
            pygame.draw.rect(display, (255, 40, 70), (pi.x - (pi.x % rez), pi.y - (pi.y % rez), rez, rez))

        
        pygame.draw.rect(display, (255, 255, 255), (cell.x, cell.y, rez, rez))
        text = font.render(str(score), 1, (255, 255, 255))
        display.blit(text, (560, 10))
        pygame.display.flip()

# ------------------------------------------------------------------------------------------------------------------------- #

if __name__ == '__main__':
    main()

