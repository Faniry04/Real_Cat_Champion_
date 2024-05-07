import pygame
from settings import *
from sprites import Generic, WildFlower, Tree
from pytmx.util_pygame import load_pygame

class Level:

    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.all_sprites = CameraGroup()
        self.collision_sprites = pygame.sprite.Group()

    def setup(self):
        tmx_data = load_pygame('import/data/final_map_.tmx')

        # fence
        for x, y, surf in tmx_data.get_layer_by_name('Fence').tiles():
            Generic((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites, LAYERS['fence'])
        # water
        for x, y, surf in tmx_data.get_layer_by_name('Water').tiles():
            Generic((x * TILE_SIZE, y * TILE_SIZE), surf, [self.all_sprites, self.collision_sprites], LAYERS['water'])

        # Decorations
        for obj in tmx_data.get_layer_by_name('Decoration'):
            WildFlower((obj.x, obj.y), obj.image, [self.all_sprites, self.collision_sprites])
        # trees
        for obj in tmx_data.get_layer_by_name('Trees'):
            Tree((obj.x, obj.y), obj.image, [self.all_sprites, self.collision_sprites], obj.name)
        # collision tiles
        for x, y, surf in tmx_data.get_layer_by_name('Collision').tiles():
            Generic((x * TILE_SIZE, y * TILE_SIZE), pygame.Surface((TILE_SIZE, TILE_SIZE)), self.collision_sprites)

        self.player = Player((960, 730), self.all_sprites, self.collision_sprites)
        Generic(pos=(0, 0),
                surf=pygame.image.load("import/graphics/world/ground.png").convert_alpha(),
                groups=self.all_sprites,
                z=LAYERS['ground'])



class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - SCREEN_WIDTH / 2
        self.offset.y = player.rect.centery - SCREEN_HEIGHT / 2

        for layer in LAYERS.values():
            for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.display_surface.blit(sprite.image, offset_rect)