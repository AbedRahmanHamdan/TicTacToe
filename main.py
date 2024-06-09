import pygame
from game import Game

# Constants
WIDTH, HEIGHT = 600, 600
BG_COLOR = (255, 255, 255)  # רקע לבן

def main():
    # Initialize Pygame
    pygame.init()

    # הגדרת תצוגה
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Tic Tac Toe')
    screen.fill(BG_COLOR)

    # הרצת משחק
    game = Game()
    game.run(screen)

if __name__ == '__main__':
    main()
