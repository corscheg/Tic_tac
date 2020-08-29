from Game import Game
import pygame
pygame.init()


def drSym(field, symbol):
    if symbol == '0':
        pict = pygame.image.load('Images/Zero.bmp')
    elif symbol == 'X':
        pict = pygame.image.load('Images/Cross.bmp')

    back.blit(pict, BUTTONS[field])


def drawWinLine(win_line):
    print(win_line)
    point1 = BUTTONS[win_line[0]].center
    point2 = BUTTONS[win_line[1]].center
    pygame.draw.line(back, RED, point1, point2, 10)
    pygame.draw.circle(back, RED, point1, 5)
    pygame.draw.circle(back, RED, point2, 5)


def turn(ps):
    if not m.get_occ(ps):
        drSym(ps, m.get_player)
    m.move(ps)


WIN_WIDTH = 640
WIN_HEIGHT = 480
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (128, 0, 0)
BUTTONS = (pygame.Rect(20, 268, 112, 112), pygame.Rect(144, 268, 112, 112), pygame.Rect(268, 268, 112, 112), pygame.Rect(20, 144, 112, 112), pygame.Rect(144, 144, 112, 112), pygame.Rect(268, 144, 112, 112), pygame.Rect(20, 20, 112, 112), pygame.Rect(144, 20, 112, 112), pygame.Rect(268, 20, 112, 112))
FPS = 30

sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
sc.fill(BLACK)
back = pygame.image.load('Images/Background.bmp')
sc.blit(back, (WIN_WIDTH // 2 - back.get_width() // 2, WIN_HEIGHT // 2 - back.get_height() // 2))
pygame.display.update()

m = Game()

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            pressed = pygame.mouse.get_pressed()
            pos = pygame.mouse.get_pos()
            if pressed[0]:
                point = pygame.Rect(pos[0] - (WIN_WIDTH // 2 - back.get_width() // 2), pos[1] - (WIN_HEIGHT // 2 - back.get_height() // 2), 1, 1)
                for i in range(len(BUTTONS)):
                    if BUTTONS[i].contains(point):
                        turn(i)
                        sc.blit(back, (WIN_WIDTH // 2 - back.get_width() // 2, WIN_HEIGHT // 2 - back.get_height() // 2))

                print(m.state)
                print(m.win_check())
                pygame.display.update()

                if m.win_check():
                    drawWinLine(m.get_win_line)
                    sc.blit(back, (WIN_WIDTH // 2 - back.get_width() // 2, WIN_HEIGHT // 2 - back.get_height() // 2))
                    pygame.display.update()
                    pygame.time.delay(5000)
                    exit()

    pygame.time.delay(1000 // FPS)

