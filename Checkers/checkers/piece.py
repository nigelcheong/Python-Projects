import pygame
from .constants import RED, WHITE, SQ_SIZE, GREY, CROWN


class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQ_SIZE * self.col + SQ_SIZE // 2
        self.y = SQ_SIZE * self.row + SQ_SIZE // 2

    def make_king(self):
        self.king = True

    def draw(self, win):
        radius = SQ_SIZE//2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)  # Draws piece outline
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)  # Draws piece

        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))  # Blit crown.png on king

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)
