import sys
import pygame
from settings import Settings

class Chess:
    """Overall class to manage game assets and behaviour"""
    def __init__(self):
        """Initialize the game"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Chess @Pratik")
    
    def run_game(self):
        """Starting the main loop for the game"""
        while True:
            # Watch for keyboard events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each passes thru loop
            self.screen.fill(self.settings.bg_color)
            self.making_board()
            self.importing_img()

            # Make the most recently drawn screen visible
            pygame.display.update()

    def making_board(self):
        for i in range(0, self.settings.length):
            for j in range(0, self.settings.length):
                if self.settings.cnt % 2 == 0:
                    pygame.draw.rect(self.screen, self.settings.white, [self.settings.size * j, self.settings.size * i, self.settings.size, self.settings.size])
                else:
                    pygame.draw.rect(self.screen, self.settings.black, [self.settings.size * j, self.settings.size * i, self.settings.size, self.settings.size])
                self.settings.cnt += 1
            self.settings.cnt -= 1

    def importing_img(self):
        self.screen.blit(self.settings.pawn_w, (self.settings.pawn_w_x, self.settings.pawn_w_y))

if __name__ == '__main__':
    # Make a game instance and run the game
    ch = Chess()
    ch.run_game()