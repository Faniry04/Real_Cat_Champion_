import pygame
from settings import *
from sprites import Generic, WildFlower, Tree
from pytmx.util_pygame import load_pygame

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()