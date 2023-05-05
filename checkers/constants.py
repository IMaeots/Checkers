import pygame

#MAIN
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS
FPS = 60

#RGB
DBLUE = (30,144,255)
LBLUE = (187,255,255)
RED = (255,0,0)
BLACK = (0,0,0)
BLUE = (0, 0, 255)

#IMGs
CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (50, 30))
WIN_BACKGROUND = pygame.transform.scale(pygame.image.load('assets/win_bg.png'), (800,800))

#SOUND
pygame.mixer.init()
SOUND = pygame.mixer.Sound('assets/sound.mp3')

#FONT
pygame.font.init()
FONT = pygame.font.SysFont("Monaco", 60)
