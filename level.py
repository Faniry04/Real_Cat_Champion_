import pygame
from settings import *
from player import Player
from sprites import *
from random import *
from pytmx.util_pygame import load_pygame


class Level:

    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.all_sprites = CameraGroup()
        self.collision_sprites = pygame.sprite.Group()
        self.increment_doumbe = 0
        self.gym_index = 0
        self.player_input = 0
        self.enemy_input = 0
        self.shop_index = 0
        self.tournament_index = 0
        self.temp_mc_health = 9999
        self.hospital_index = 0
        self.font1 = pygame.font.Font('import/font/pixel2.ttf', 50)
        self.first_enemy_index = 0
        self.money_win = 0
        self.temp_cowboy_health = 0

        self.mc = MainCharacter()

        self.setup()

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

    def gym_interaction(self, dt):

        if self.gym_index == 1:
            self.player.pos.x = 1070
            self.player.pos.y = 1940

        if (1000 <= self.player.rect.centerx <= 1100) and (2000 >= self.player.rect.centery >= 1870):
            for event2 in pygame.event.get():
                if event2.type == pygame.KEYDOWN and event2.key == pygame.K_TAB:
                    if self.gym_index != 1:
                        # initialisation des PV de tous les personnages (ennemies et mc)
                        self.temp_mc_health = self.mc.health
                        self.temp_trainingdummy_health = 10
                        self.temp_cowboy_health = 7
                        self.tournament_index = 1

                        self.round_display = Generic(pos=(825, 2120),
                                                     surf=self.font1.render(
                                                         'ROUND 1', False, (244, 222, 7)),
                                                     groups=self.all_sprites,
                                                     z=LAYERS['text'])
                        self.background_gym = Generic(pos=(430, 1580),
                                                      surf=pygame.image.load(
                                                          "import/graphics/ecrans/ecran_combat11.png").convert_alpha(),
                                                      groups=self.all_sprites,
                                                      z=LAYERS['screen'])

                        self.enemy_display = Generic(pos=(830, 1480),
                                                     surf=pygame.image.load(
                                                         "import/graphics/combat_cats/training_dummy.png").convert_alpha(),
                                                     groups=self.all_sprites,
                                                     z=LAYERS['combat_cat'])

                        self.mc_display = Generic(pos=(710, 1480),
                                                  surf=pygame.image.load(
                                                      "import/graphics/combat_cats/mc_idle.png").convert_alpha(),
                                                  groups=self.all_sprites,
                                                  z=LAYERS['combat_cat'])
                        self.mc_health_display = Generic(pos=(825, 2180),
                                                         surf=self.font1.render(
                                                             'TES PV:' + str(self.temp_mc_health) + '/' + str(
                                                                 self.mc.health), False, (255, 255, 255)),
                                                         groups=self.all_sprites,
                                                         z=LAYERS['text'])
                        self.enemy_health_display = Generic(pos=(1250, 2180),
                                                            surf=self.font1.render('PV ENNEMIS:', False,
                                                                                   (255, 255, 255)),
                                                            groups=self.all_sprites,
                                                            z=LAYERS['text'])

                    self.gym_index = 1
                    self.player.pos.x = 1070
                    self.player.pos.y = 1940

                if self.tournament_index == 1:  # first enemy : training dummy

                    if event2.type == pygame.KEYDOWN and event2.key == pygame.K_1:
                        self.enemy_health_display.kill()
                        self.mc_health_display.kill()
                        self.mc_display.kill()
                        self.enemy_display.kill()

                        self.enemy_display = Generic(pos=(830, 1480),
                                                     surf=pygame.image.load(
                                                         "import/graphics/combat_cats/training_dummy.png").convert_alpha(),
                                                     groups=self.all_sprites,
                                                     z=LAYERS['combat_cat'])
                        self.mc_display = Generic(pos=(710, 1480),
                                                  surf=pygame.image.load(
                                                      "import/graphics/combat_cats/mc_punch.png").convert_alpha(),
                                                  groups=self.all_sprites,
                                                  z=LAYERS['combat_cat'])

                        self.temp_trainingdummy_health = self.temp_trainingdummy_health - self.mc.damage

                        self.mc_health_display = Generic(pos=(825, 2180),
                                                         surf=self.font1.render(
                                                             'TES PV:' + str(self.temp_mc_health) + '/' + str(
                                                                 self.mc.health), False, (255, 255, 255)),
                                                         groups=self.all_sprites,
                                                         z=LAYERS['text'])
                        self.enemy_health_display = Generic(pos=(1250, 2180),
                                                            surf=self.font1.render('PV ENNEMIS:' + str(
                                                                self.temp_trainingdummy_health) + '/10', False,
                                                                                   (255, 255, 255)),
                                                            groups=self.all_sprites,
                                                            z=LAYERS['text'])

                    if event2.type == pygame.KEYDOWN and event2.key == pygame.K_2:
                        self.enemy_health_display.kill()
                        self.mc_health_display.kill()
                        self.mc_display.kill()
                        self.enemy_display.kill()
                        self.enemy_display = Generic(pos=(830, 1480),
                                                     surf=pygame.image.load(
                                                         "import/graphics/combat_cats/training_dummy.png").convert_alpha(),
                                                     groups=self.all_sprites,
                                                     z=LAYERS['combat_cat'])
                        self.mc_display = Generic(pos=(740, 1480),
                                                  surf=pygame.image.load(
                                                      "import/graphics/combat_cats/mc_kick.png").convert_alpha(),
                                                  groups=self.all_sprites,
                                                  z=LAYERS['combat_cat'])
                        self.temp_trainingdummy_health = self.temp_trainingdummy_health - self.mc.damage
                        self.mc_health_display = Generic(pos=(825, 2180),
                                                         surf=self.font1.render(
                                                             'TES PV:' + str(self.temp_mc_health) + '/' + str(
                                                                 self.mc.health), False, (255, 255, 255)),
                                                         groups=self.all_sprites,
                                                         z=LAYERS['text'])
                        self.enemy_health_display = Generic(pos=(1250, 2180),
                                                            surf=self.font1.render('PV ENNEMIS:' + str(
                                                                self.temp_trainingdummy_health) + '/10', False,
                                                                                   (255, 255, 255)),
                                                            groups=self.all_sprites,
                                                            z=LAYERS['text'])

                    if event2.type == pygame.KEYDOWN and event2.key == pygame.K_3:
                        self.enemy_health_display.kill()
                        self.mc_health_display.kill()
                        self.mc_display.kill()
                        self.enemy_display.kill()
                        self.enemy_display = Generic(pos=(830, 1480),
                                                     surf=pygame.image.load(
                                                         "import/graphics/combat_cats/training_dummy.png").convert_alpha(),
                                                     groups=self.all_sprites,
                                                     z=LAYERS['combat_cat'])
                        self.mc_display = Generic(pos=(690, 1480),
                                                  surf=pygame.image.load(
                                                      "import/graphics/combat_cats/mc_protection.png").convert_alpha(),
                                                  groups=self.all_sprites,
                                                  z=LAYERS['combat_cat'])
                        self.mc_health_display = Generic(pos=(825, 2180),
                                                         surf=self.font1.render(
                                                             'TES PV:' + str(self.temp_mc_health) + '/' + str(
                                                                 self.mc.health), False, (255, 255, 255)),
                                                         groups=self.all_sprites,
                                                         z=LAYERS['text'])
                        self.enemy_health_display = Generic(pos=(1250, 2180),
                                                            surf=self.font1.render('PV ENNEMIS:' + str(
                                                                self.temp_trainingdummy_health) + '/10', False,
                                                                                   (255, 255, 255)),
                                                            groups=self.all_sprites,
                                                            z=LAYERS['text'])

                    if self.temp_trainingdummy_health <= 0:
                        self.temp_mc_health = self.mc.health
                        self.enemy_health_display.kill()
                        self.mc_display.kill()
                        self.enemy_display.kill()
                        self.mc_health_display.kill()
                        self.enemy_input = 0
                        self.player_input = 0
                        self.round_display.kill()
                        self.tournament_index = 2
                        self.money_win = 1

                if self.tournament_index == 2 and self.first_enemy_index == 1:  # second enemy : cowboy

                    if event2.type == pygame.KEYDOWN and event2.key == pygame.K_SPACE:
                        self.background_gym.kill()
                        self.enemy_display.kill()
                        self.mc_display.kill()
                        self.gym_index = 0
                        self.player_input = 0
                        self.enemy_input = 0

                    if event2.type == pygame.KEYDOWN and event2.key == pygame.K_1:
                        self.enemy_input = randint(1, 3)
                        if self.enemy_input == 1:
                            self.enemy_display.kill()
                            self.mc_display.kill()

                            self.enemy_display = Generic(pos=(830, 1480),
                                                         surf=pygame.image.load(
                                                             "import/graphics/combat_cats/cb_punch.png").convert_alpha(),
                                                         groups=self.all_sprites,
                                                         z=LAYERS['combat_cat'])

                            self.mc_display = Generic(pos=(710, 1480),
                                                      surf=pygame.image.load(
                                                          "import/graphics/combat_cats/mc_punch.png").convert_alpha(),
                                                      groups=self.all_sprites,
                                                      z=LAYERS['combat_cat'])
                        if self.enemy_input == 2:
                            self.enemy_display.kill()
                            self.mc_display.kill()

                            self.mc_display = Generic(pos=(740, 1480),
                                                      surf=pygame.image.load(
                                                          "import/graphics/combat_cats/mc_punch.png").convert_alpha(),
                                                      groups=self.all_sprites,
                                                      z=LAYERS['combat_cat'])

                            self.enemy_display = Generic(pos=(860, 1480),
                                                         surf=pygame.image.load(
                                                             "import/graphics/combat_cats/cb_kick.png").convert_alpha(),
                                                         groups=self.all_sprites,
                                                         z=LAYERS['combat_cat'])
                            self.temp_cowboy_health = self.temp_cowboy_health - self.mc.damage
                            self.mc_health_display.kill()
                            self.enemy_health_display.kill()
                            self.mc_health_display = Generic(pos=(825, 2180),
                                                             surf=self.font1.render(
                                                                 'TES PV:' + str(self.temp_mc_health) + '/' + str(
                                                                     self.mc.health), False, (255, 255, 255)),
                                                             groups=self.all_sprites,
                                                             z=LAYERS['text'])
                            self.enemy_health_display = Generic(pos=(1250, 2180),
                                                                surf=self.font1.render('PV ENNEMIS:' + str(
                                                                    self.temp_cowboy_health) + '/7', False,
                                                                                       (255, 255, 255)),
                                                                groups=self.all_sprites,
                                                                z=LAYERS['text'])
                        if self.enemy_input == 3:
                            self.enemy_display.kill()
                            self.mc_display.kill()

                            self.mc_display = Generic(pos=(710, 1480),
                                                      surf=pygame.image.load(
                                                          "import/graphics/combat_cats/mc_punch.png").convert_alpha(),
                                                      groups=self.all_sprites,
                                                      z=LAYERS['combat_cat'])

                            self.enemy_display = Generic(pos=(870, 1480),
                                                         surf=pygame.image.load(
                                                             "import/graphics/combat_cats/cb_protection.png").convert_alpha(),
                                                         groups=self.all_sprites,
                                                         z=LAYERS['combat_cat'])
                            self.temp_mc_health = self.temp_mc_health - 1
                            self.mc_health_display.kill()
                            self.enemy_health_display.kill()
                            self.mc_health_display = Generic(pos=(825, 2180),
                                                             surf=self.font1.render(
                                                                 'TES PV:' + str(self.temp_mc_health) + '/' + str(
                                                                     self.mc.health), False, (255, 255, 255)),
                                                             groups=self.all_sprites,
                                                             z=LAYERS['text'])
                            self.enemy_health_display = Generic(pos=(1250, 2180),
                                                                surf=self.font1.render('PV ENNEMIS:' + str(
                                                                    self.temp_cowboy_health) + '/7', False,
                                                                                       (255, 255, 255)),
                                                                groups=self.all_sprites,
                                                                z=LAYERS['text'])

                    if event2.type == pygame.KEYDOWN and event2.key == pygame.K_2:
                        self.enemy_input = randint(1, 3)
                        if self.enemy_input == 1:
                            self.enemy_display.kill()
                            self.mc_display.kill()

                            self.mc_display = Generic(pos=(740, 1480),
                                                      surf=pygame.image.load(
                                                          "import/graphics/combat_cats/mc_kick.png").convert_alpha(),
                                                      groups=self.all_sprites,
                                                      z=LAYERS['combat_cat'])

                            self.enemy_display = Generic(pos=(860, 1480),
                                                         surf=pygame.image.load(
                                                             "import/graphics/combat_cats/cb_punch.png").convert_alpha(),
                                                         groups=self.all_sprites,
                                                         z=LAYERS['combat_cat'])
                            self.temp_mc_health = self.temp_mc_health - 1
                            self.mc_health_display.kill()
                            self.enemy_health_display.kill()
                            self.mc_health_display = Generic(pos=(825, 2180),
                                                             surf=self.font1.render(
                                                                 'TES PV:' + str(self.temp_mc_health) + '/' + str(
                                                                     self.mc.health), False, (255, 255, 255)),
                                                             groups=self.all_sprites,
                                                             z=LAYERS['text'])
                            self.enemy_health_display = Generic(pos=(1250, 2180),
                                                                surf=self.font1.render('PV ENNEMIS:' + str(
                                                                    self.temp_cowboy_health) + '/7', False,
                                                                                       (255, 255, 255)),
                                                                groups=self.all_sprites,
                                                                z=LAYERS['text'])
                        if self.enemy_input == 2:
                            self.enemy_display.kill()
                            self.mc_display.kill()

                            self.mc_display = Generic(pos=(740, 1480),
                                                      surf=pygame.image.load(
                                                          "import/graphics/combat_cats/mc_kick.png").convert_alpha(),
                                                      groups=self.all_sprites,
                                                      z=LAYERS['combat_cat'])

                            self.enemy_display = Generic(pos=(860, 1480),
                                                         surf=pygame.image.load(
                                                             "import/graphics/combat_cats/cb_kick.png").convert_alpha(),
                                                         groups=self.all_sprites,
                                                         z=LAYERS['combat_cat'])
                        if self.enemy_input == 3:
                            self.enemy_display.kill()
                            self.mc_display.kill()

                            self.enemy_display = Generic(pos=(880, 1480),
                                                         surf=pygame.image.load(
                                                             "import/graphics/combat_cats/cb_protection.png").convert_alpha(),
                                                         groups=self.all_sprites,
                                                         z=LAYERS['combat_cat'])

                            self.mc_display = Generic(pos=(740, 1480),
                                                      surf=pygame.image.load(
                                                          "import/graphics/combat_cats/mc_kick.png").convert_alpha(),
                                                      groups=self.all_sprites,
                                                      z=LAYERS['combat_cat'])
                            self.temp_cowboy_health = self.temp_cowboy_health - self.mc.damage
                            self.mc_health_display.kill()
                            self.enemy_health_display.kill()
                            self.mc_health_display = Generic(pos=(825, 2180),
                                                             surf=self.font1.render(
                                                                 'TES PV:' + str(self.temp_mc_health) + '/' + str(
                                                                     self.mc.health), False, (255, 255, 255)),
                                                             groups=self.all_sprites,
                                                             z=LAYERS['text'])
                            self.enemy_health_display = Generic(pos=(1250, 2180),
                                                                surf=self.font1.render('PV ENNEMIS:' + str(
                                                                    self.temp_cowboy_health) + '/7', False,
                                                                                       (255, 255, 255)),
                                                                groups=self.all_sprites,
                                                                z=LAYERS['text'])

                    if event2.type == pygame.KEYDOWN and event2.key == pygame.K_3:

                        self.enemy_input = randint(1, 3)
                        if self.enemy_input == 1:
                            self.enemy_display.kill()
                            self.mc_display.kill()

                            self.enemy_display = Generic(pos=(830, 1480),
                                                         surf=pygame.image.load(
                                                             "import/graphics/combat_cats/cb_punch.png").convert_alpha(),
                                                         groups=self.all_sprites,
                                                         z=LAYERS['combat_cat'])

                            self.mc_display = Generic(pos=(690, 1480),
                                                      surf=pygame.image.load(
                                                          "import/graphics/combat_cats/mc_protection.png").convert_alpha(),
                                                      groups=self.all_sprites,
                                                      z=LAYERS['combat_cat'])
                            self.temp_cowboy_health = self.temp_cowboy_health - self.mc.damage
                            self.mc_health_display.kill()
                            self.enemy_health_display.kill()
                            self.mc_health_display = Generic(pos=(825, 2180),
                                                             surf=self.font1.render(
                                                                 'TES PV:' + str(self.temp_mc_health) + '/' + str(
                                                                     self.mc.health), False, (255, 255, 255)),
                                                             groups=self.all_sprites,
                                                             z=LAYERS['text'])
                            self.enemy_health_display = Generic(pos=(1250, 2180),
                                                                surf=self.font1.render('PV ENNEMIS:' + str(
                                                                    self.temp_cowboy_health) + '/7', False,
                                                                                       (255, 255, 255)),
                                                                groups=self.all_sprites,
                                                                z=LAYERS['text'])
                        if self.enemy_input == 2:
                            self.enemy_display.kill()
                            self.mc_display.kill()

                            self.enemy_display = Generic(pos=(870, 1480),
                                                         surf=pygame.image.load(
                                                             "import/graphics/combat_cats/cb_kick.png").convert_alpha(),
                                                         groups=self.all_sprites,
                                                         z=LAYERS['combat_cat'])

                            self.mc_display = Generic(pos=(680, 1480),
                                                      surf=pygame.image.load(
                                                          "import/graphics/combat_cats/mc_protection.png").convert_alpha(),
                                                      groups=self.all_sprites,
                                                      z=LAYERS['combat_cat'])
                            self.temp_mc_health = self.temp_mc_health - 1
                            self.mc_health_display.kill()
                            self.enemy_health_display.kill()
                            self.mc_health_display = Generic(pos=(825, 2180),
                                                             surf=self.font1.render(
                                                                 'TES PV:' + str(self.temp_mc_health) + '/' + str(
                                                                     self.mc.health), False, (255, 255, 255)),
                                                             groups=self.all_sprites,
                                                             z=LAYERS['text'])
                            self.enemy_health_display = Generic(pos=(1250, 2180),
                                                                surf=self.font1.render('PV ENNEMIS:' + str(
                                                                    self.temp_cowboy_health) + '/7', False,
                                                                                       (255, 255, 255)),
                                                                groups=self.all_sprites,
                                                                z=LAYERS['text'])
                        if self.enemy_input == 3:
                            self.enemy_display.kill()
                            self.mc_display.kill()

                            self.mc_display = Generic(pos=(740, 1480),
                                                      surf=pygame.image.load(
                                                          "import/graphics/combat_cats/mc_protection.png").convert_alpha(),
                                                      groups=self.all_sprites,
                                                      z=LAYERS['combat_cat'])

                            self.enemy_display = Generic(pos=(830, 1480),
                                                         surf=pygame.image.load(
                                                             "import/graphics/combat_cats/cb_protection.png").convert_alpha(),
                                                         groups=self.all_sprites,
                                                         z=LAYERS['combat_cat'])

                        if self.tournament_index == 2 and self.first_enemy_index == 0:
                            self.mc_display = Generic(pos=(710, 1480),
                                                      surf=pygame.image.load(
                                                          "import/graphics/combat_cats/mc_idle.png").convert_alpha(),
                                                      groups=self.all_sprites,
                                                      z=LAYERS['combat_cat'])
                            self.enemy_display = Generic(pos=(830, 1480),
                                                         surf=pygame.image.load(
                                                             "import/graphics/combat_cats/cb_idle.png").convert_alpha(),
                                                         groups=self.all_sprites,
                                                         z=LAYERS['combat_cat'])
                            self.mc_health_display = Generic(pos=(825, 2180),
                                                             surf=self.font1.render(
                                                                 'TES PV:' + str(self.temp_mc_health) + '/' + str(
                                                                     self.mc.health), False, (255, 255, 255)),
                                                             groups=self.all_sprites,
                                                             z=LAYERS['text'])
                            self.enemy_health_display = Generic(pos=(1250, 2180),
                                                                surf=self.font1.render('PV ENNEMIS:' + str(
                                                                    self.temp_cowboy_health) + '/7', False,
                                                                                       (255, 255, 255)),
                                                                groups=self.all_sprites,
                                                                z=LAYERS['text'])
                            self.first_enemy_index = 1

                if self.tournament_index == 2 and self.first_enemy_index == 0:
                    self.mc_display = Generic(pos=(710, 1480),
                                              surf=pygame.image.load(
                                                  "import/graphics/combat_cats/mc_idle.png").convert_alpha(),
                                              groups=self.all_sprites,
                                              z=LAYERS['combat_cat'])
                    self.enemy_display = Generic(pos=(830, 1480),
                                                 surf=pygame.image.load(
                                                     "import/graphics/combat_cats/cb_idle.png").convert_alpha(),
                                                 groups=self.all_sprites,
                                                 z=LAYERS['combat_cat'])
                    self.mc_health_display = Generic(pos=(825, 2180),
                                                     surf=self.font1.render(
                                                         'TES PV:' + str(self.temp_mc_health) + '/' + str(
                                                             self.mc.health), False, (255, 255, 255)),
                                                     groups=self.all_sprites,
                                                     z=LAYERS['text'])
                    self.enemy_health_display = Generic(pos=(1250, 2180),
                                                        surf=self.font1.render('PV ENNEMIS:' + str(
                                                            self.temp_cowboy_health) + '/7', False,
                                                                               (255, 255, 255)),
                                                        groups=self.all_sprites,
                                                        z=LAYERS['text'])
                    self.round_display = Generic(pos=(825, 2120),
                                                 surf=self.font1.render(
                                                     'ROUND 2', False, (244, 222, 7)),
                                                 groups=self.all_sprites,
                                                 z=LAYERS['text'])

                    self.first_enemy_index = 1

                if self.temp_cowboy_health <= 0:
                    self.money_win = 3

                if self.temp_mc_health <= 0:
                    if self.hospital_index == 0:
                        self.death_backround = Generic(pos=(430, 1580),
                                                       surf=pygame.image.load(
                                                           "import/graphics/ecrans/ecran_mort1.png").convert_alpha(),
                                                       groups=self.all_sprites,
                                                       z=LAYERS['victory_screen'])
                        self.hospital_index = 1
                    if event2.type == pygame.KEYDOWN and event2.key == pygame.K_SPACE:
                        self.ko()

    def shop_interaction(self, dt):
        self.font = pygame.font.Font('import/font/pixel2.ttf', 80)
        if self.shop_index == 1:
            self.player.pos.x = 1500
            self.player.pos.y = 1300

        if (1450 <= self.player.rect.centerx <= 1550) and (1320 >= self.player.rect.centery >= 1110):
            for event2 in pygame.event.get():
                if event2.type == pygame.KEYDOWN and event2.key == pygame.K_TAB:
                    if self.shop_index != 1:
                        self.background_shop = Generic(pos=(860, 940),
                                                       surf=pygame.image.load(
                                                           "import/graphics/ecrans/ecran_shop.png").convert_alpha(),
                                                       groups=self.all_sprites,
                                                       z=LAYERS['screen'])
                        self.health_display = Generic(pos=(1318, 1457),
                                                      surf=self.font.render(str(self.mc.health), False,
                                                                            (255, 255, 255)),
                                                      groups=self.all_sprites,
                                                      z=LAYERS['text'])

                        self.damage_display = Generic(pos=(1740, 1457),
                                                      surf=self.font.render(str(self.mc.damage), False,
                                                                            (255, 255, 255)),
                                                      groups=self.all_sprites,
                                                      z=LAYERS['text'])

                        self.money_display = Generic(pos=(1640, 1550),
                                                     surf=self.font.render(str(self.mc.money) + ' $', False,
                                                                           (255, 255, 255)),
                                                     groups=self.all_sprites,
                                                     z=LAYERS['text'])
                    self.shop_index = 1
                    self.player.pos.x = 1500
                    self.player.pos.y = 1300

                if event2.type == pygame.KEYDOWN and event2.key == pygame.K_ESCAPE:
                    self.background_shop.kill()
                    self.damage_display.kill()
                    self.health_display.kill()
                    self.money_display.kill()
                    self.shop_index = 0

                if event2.type == pygame.KEYDOWN and event2.key == pygame.K_1:
                    self.damage_display.kill()
                    self.health_display.kill()
                    self.money_display.kill()

                    self.mc.potion_de_vie()
                    self.health_display = Generic(pos=(1318, 1457),
                                                  surf=self.font.render(str(self.mc.health), False, (255, 255, 255)),
                                                  groups=self.all_sprites,
                                                  z=LAYERS['text'])

                    self.damage_display = Generic(pos=(1740, 1457),
                                                  surf=self.font.render(str(self.mc.damage), False, (255, 255, 255)),
                                                  groups=self.all_sprites,
                                                  z=LAYERS['text'])

                    self.money_display = Generic(pos=(1640, 1550),
                                                 surf=self.font.render(str(self.mc.money) + ' $', False,
                                                                       (255, 255, 255)),
                                                 groups=self.all_sprites,
                                                 z=LAYERS['text'])

                if event2.type == pygame.KEYDOWN and event2.key == pygame.K_2:
                    self.damage_display.kill()
                    self.health_display.kill()
                    self.money_display.kill()
                    self.mc.potion_de_force()
                    self.health_display = Generic(pos=(1318, 1457),
                                                  surf=self.font.render(str(self.mc.health), False, (255, 255, 255)),
                                                  groups=self.all_sprites,
                                                  z=LAYERS['text'])

                    self.damage_display = Generic(pos=(1740, 1457),
                                                  surf=self.font.render(str(self.mc.damage), False, (255, 255, 255)),
                                                  groups=self.all_sprites,
                                                  z=LAYERS['text'])

                    self.money_display = Generic(pos=(1640, 1550),
                                                 surf=self.font.render(str(self.mc.money) + ' $', False,
                                                                       (255, 255, 255)),
                                                 groups=self.all_sprites,
                                                 z=LAYERS['text'])

                if event2.type == pygame.KEYDOWN and event2.key == pygame.K_3:
                    self.damage_display.kill()
                    self.health_display.kill()
                    self.money_display.kill()
                    self.mc.pasteque()
                    self.health_display = Generic(pos=(1318, 1457),
                                                  surf=self.font.render(str(self.mc.health), False, (255, 255, 255)),
                                                  groups=self.all_sprites,
                                                  z=LAYERS['text'])

                    self.damage_display = Generic(pos=(1740, 1457),
                                                  surf=self.font.render(str(self.mc.damage), False, (255, 255, 255)),
                                                  groups=self.all_sprites,
                                                  z=LAYERS['text'])

                    self.money_display = Generic(pos=(1640, 1550),
                                                 surf=self.font.render(str(self.mc.money) + ' $', False,
                                                                       (255, 255, 255)),
                                                 groups=self.all_sprites,
                                                 z=LAYERS['text'])

                if event2.type == pygame.KEYDOWN and event2.key == pygame.K_4:
                    self.damage_display.kill()
                    self.health_display.kill()
                    self.money_display.kill()
                    self.mc.fruit_du_diable()
                    self.health_display = Generic(pos=(1318, 1457),
                                                  surf=self.font.render(str(self.mc.health), False, (255, 255, 255)),
                                                  groups=self.all_sprites,
                                                  z=LAYERS['text'])

                    self.damage_display = Generic(pos=(1740, 1457),
                                                  surf=self.font.render(str(self.mc.damage), False, (255, 255, 255)),
                                                  groups=self.all_sprites,
                                                  z=LAYERS['text'])

                    self.money_display = Generic(pos=(1640, 1550),
                                                 surf=self.font.render(str(self.mc.money) + ' $', False,
                                                                       (255, 255, 255)),
                                                 groups=self.all_sprites,
                                                 z=LAYERS['text'])

    def ko(self):
        self.background_gym.kill()
        self.enemy_display.kill()
        self.mc_display.kill()
        self.enemy_health_display.kill()
        self.mc_health_display.kill()
        self.round_display.kill()
        self.death_backround.kill()
        self.tournament_index = 0
        self.gym_index = 0
        self.player_input = 0
        self.enemy_input = 0
        self.hospital_index = 0
        self.first_enemy_index = 0
        self.mc.money = self.mc.money + self.money_win
        self.money_win = 0
        self.player.pos.x = 950
        self.player.pos.y = 1300
        self.temp_mc_health = self.mc.health

    def run(self, dt):
        self.display_surface.fill('black')
        self.all_sprites.custom_draw(self.player)
        self.all_sprites.update(dt)
        self.doumbe_interaction(dt)
        self.gym_interaction(dt)
        self.shop_interaction(dt)


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


class MainCharacter():
    def __init__(self):
        super().__init__()
        self.health = 5
        self.damage = 1
        self.money = 1000

    def potion_de_vie(self):
        if self.money >= 5:
            self.money = self.money - 5
            self.health = self.health + 1

    def potion_de_force(self):
        if self.money >= 5:
            self.money = self.money - 5
            self.damage = self.damage + 1

    def pasteque(self):
        if self.money >= 30:
            self.money = self.money - 30
            self.damage = self.damage + 5
            self.health = self.health + 5

    def fruit_du_diable(self):
        self.fruit_index = randint(1, 5)
        if self.money >= 70:
            self.money = self.money - 70
            if self.fruit_index == 1:
                self.damage = int(self.damage * 2)
                self.health = int(self.health * 2)
            if self.fruit_index == 2:
                self.damage = self.damage + 10
                self.health = self.health + 10
            if self.fruit_index == 3:
                self.damage = self.damage + 5
                self.health = self.health + 50
            if self.fruit_index == 4:
                self.damage = int(self.damage / 2)
                self.health = int(self.health / 2)
            if self.fruit_index == 5:
                self.damage = self.damage + 100
                self.health = self.health + 100



































