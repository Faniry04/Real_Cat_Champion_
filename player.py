import pygame
from settings import *

class Player(pygame.sprite.Sprite):
	def __init__(self, pos, group, collision_sprites):
		super().__init__(group)


		self.status = 'down_idle'
		self.frame_index = 0

		# general setup
		self.import_assets()
		self.image = self.animations[self.status][self.frame_index]
		self.rect = self.image.get_rect(center = pos)
		self.z = LAYERS['main']

		# movement attributes
		self.import_assets()
		self.direction = pygame.math.Vector2()
		self.pos = pygame.math.Vector2(self.rect.center)
		self.speed = 200


		#collision

		self.hitbox = self.rect.copy().inflate((-126, -70))
		self.collision_sprites = collision_sprites