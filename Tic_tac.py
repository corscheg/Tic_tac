from Game import Game
import pygame
pygame.init()


def drCym(field, symbol):
    imga = pygame.Surface((100, 100))
    imga.fill((0, 200, 0))
    # if symbol == '0':
    #     img = pygame.image.load('Images/Zero.bmp')
    # elif symbol == 'X':
    #     img = pygame.image.load('Images/Zero.bmp')

    print(BUTTONS[field])
    print(imga)
    back.blit(imga, BUTTONS[field])
    pygame.display.update()


def turn(plr, ps):
    m.move(ps, player)
    if not m.get_occ:
        drCym(ps, player)


WIN_WIDTH = 640
WIN_HEIGHT = 480
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTONS = (pygame.Rect(20, 268, 112, 112), pygame.Rect(144, 268, 112, 112), pygame.Rect(268, 268, 112, 112), pygame.Rect(20, 144, 112, 112), pygame.Rect(144, 144, 112, 112), pygame.Rect(268, 144, 112, 112), pygame.Rect(20, 20, 112, 112), pygame.Rect(144, 20, 112, 112), pygame.Rect(268, 20, 112, 112))
FPS = 30

sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
sc.fill(BLACK)
back = pygame.image.load('Images/Background.bmp')
sc.blit(back, (WIN_WIDTH // 2 - back.get_width() // 2, WIN_HEIGHT // 2 - back.get_height() // 2))
img = pygame.Surface((100, 100))
img.fill((255, 255, 255))
back.blit(img, (0, 0))
pygame.display.update()

player = '0'
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
                        turn(player, i)

                if player == '0':
                    player = 'X'
                elif player == 'X':
                    player = '0'

                print(m.state)
                pygame.display.update()

                if m.win_check():
                    exit()

    pygame.time.delay(1000 // FPS)

