import pygame

class Settings:
    """A class to store all settings for the game"""

    def __init__(self):
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Board settings
        self.size = 75
        self.length = 8
        self.cnt = 0
        self.white = (207, 237, 173)
        self.black = (209, 165, 71)

        """Adding images inside the cells"""
        self.pawn_w = pygame.image.load('icons/pawn_w.png')
        # self.icon_b = pygame.image.load('pawm_b.png')
        self.pawn_w_x = 21.5
        self.pawn_w_y = 21.5 + 75