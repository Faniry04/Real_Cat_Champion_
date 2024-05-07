import pygame
import sys

from settings import *
from level import Level


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Real Cat Champion')
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.game_active = 0
    def run(self):

        while self.game_active ==0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.game_active = 1

            ecran_start = pygame.image.load('import/graphics/ecrans/ecran_start.png').convert()
            self.screen.blit(ecran_start, (0, 0))
            pygame.display.update()


        while self.game_active == 1:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                dt = self.clock.tick() / 1000
                self.level.run(dt)
                pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()