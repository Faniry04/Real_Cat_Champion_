import pygame
import sys

from settings import *



class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Real Cat Champion')
        self.clock = pygame.time.Clock()


if __name__ == '__main__':
    game = Game()
    game.run()