import pygame
from settings import *
from player import Player
from sprites import *
from pytmx.util_pygame import load_pygame


class Level:

    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.all_sprites = CameraGroup()
        self.collision_sprites = pygame.sprite.Group()
        self.increment_doumbe = 0
        self.setup()

    def setup(self):
        # ajout des differents elements à partir du fichier tiled

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

    def doumbe_interaction(self, dt):
        keys = pygame.key.get_pressed()

        if (900 <= self.player.rect.centerx <= 1000) and (2100 >= self.player.rect.centery >= 1800):
            for event1 in pygame.event.get():
                if event1.type == pygame.KEYDOWN and event1.key == pygame.K_SPACE:
                    self.increment_doumbe += 1

                    if self.increment_doumbe == 1:
                        self.dialogue1 = Dialogue(pos=(680, 1750),
                                                  surf=pygame.image.load(
                                                      "import/graphics/dialogue/dialogue1_.png").convert_alpha(),
                                                  groups=self.all_sprites,
                                                  z=LAYERS['dialogue'])

                    if self.increment_doumbe == 2:
                        self.dialogue1.kill()
                        self.dialogue2 = Dialogue(pos=(680, 1750),
                                                  surf=pygame.image.load(
                                                      "import/graphics/dialogue/dialogue2_.png").convert_alpha(),
                                                  groups=self.all_sprites,
                                                  z=LAYERS['dialogue'])

                    if self.increment_doumbe == 3:
                        self.dialogue2.kill()
                        self.dialogue3 = Dialogue(pos=(680, 1750),
                                                  surf=pygame.image.load(
                                                      "import/graphics/dialogue/dialogue3_.png").convert_alpha(),
                                                  groups=self.all_sprites,
                                                  z=LAYERS['dialogue'])

                    if self.increment_doumbe == 4:
                        self.dialogue3.kill()
                        self.dialogue4 = Dialogue(pos=(680, 1750),
                                                  surf=pygame.image.load(
                                                      "import/graphics/dialogue/dialogue4_.png").convert_alpha(),
                                                  groups=self.all_sprites,
                                                  z=LAYERS['dialogue'])

                    if self.increment_doumbe == 5:
                        self.dialogue4.kill()
                        self.dialogue5 = Dialogue(pos=(680, 1750),
                                                  surf=pygame.image.load(
                                                      "import/graphics/dialogue/dialogue5_.png").convert_alpha(),
                                                  groups=self.all_sprites,
                                                  z=LAYERS['dialogue'])

                    if self.increment_doumbe == 6:
                        self.dialogue5.kill()
                        self.dialogue6 = Dialogue(pos=(680, 1750),
                                                  surf=pygame.image.load(
                                                      "import/graphics/dialogue/dialogue6_.png").convert_alpha(),
                                                  groups=self.all_sprites,
                                                  z=LAYERS['dialogue'])
                    if self.increment_doumbe == 7:
                        self.dialogue6.kill()
                        self.increment_doumbe = 0

    def run(self, dt):
        self.display_surface.fill('black')
        self.all_sprites.custom_draw(self.player)
        self.all_sprites.update(dt)
        self.doumbe_interaction(dt)


class CameraGroup(pygame.sprite.Group):
    # cette classe sert pour que la camera suit le joueur dans ses deplacements
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

