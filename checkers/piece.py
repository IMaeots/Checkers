import pygame
from .constants import BLACK, SQUARE_SIZE, CROWN

# ALL ABOUT CHECKER PIECES
class Piece:
    PADDING = 10

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True

    def draw(self, SCREEN):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(SCREEN, self.color, (self.x, self.y), radius)
        if self.king:
            SCREEN.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()


    # Error = color
    def __repr__(self):
        return str(self.color)