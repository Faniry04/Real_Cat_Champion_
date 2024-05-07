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


	def import_assets(self):
		self.animations = {'up': [[], [], [], []], 'down': [[], [], [], []], 'left': [[], [], [], []],'right': [[], [], [], []],
						   'up_idle': [[], []], 'down_idle': [[], []], 'left_idle': [[], []], 'right_idle': [[], []]}

		self.animations['up'][0] = pygame.image.load("import/graphics/character/up/0.png").convert_alpha()
		self.animations['up'][1] = pygame.image.load('import/graphics/character/up/1.png').convert_alpha()
		self.animations['up'][2] = pygame.image.load('import/graphics/character/up/2.png').convert_alpha()
		self.animations['up'][3] = pygame.image.load('import/graphics/character/up/3.png').convert_alpha()
		self.animations['down'][0] = pygame.image.load('import/graphics/character/down/0.png').convert_alpha()
		self.animations['down'][1] = pygame.image.load('import/graphics/character/down/1.png').convert_alpha()
		self.animations['down'][2] = pygame.image.load('import/graphics/character/down/2.png').convert_alpha()
		self.animations['down'][3] = pygame.image.load('import/graphics/character/down/3.png').convert_alpha()
		self.animations['right'][0] = pygame.image.load('import/graphics/character/right/0.png').convert_alpha()
		self.animations['right'][1] = pygame.image.load('import/graphics/character/right/1.png').convert_alpha()
		self.animations['right'][2] = pygame.image.load('import/graphics/character/right/2.png').convert_alpha()
		self.animations['right'][3] = pygame.image.load('import/graphics/character/right/3.png').convert_alpha()
		self.animations['left'][0] = pygame.image.load('import/graphics/character/left/0.png').convert_alpha()
		self.animations['left'][1] = pygame.image.load('import/graphics/character/left/1.png').convert_alpha()
		self.animations['left'][2] = pygame.image.load('import/graphics/character/left/2.png').convert_alpha()
		self.animations['left'][3] = pygame.image.load('import/graphics/character/left/3.png').convert_alpha()
		self.animations['up_idle'][0] = pygame.image.load("import/graphics/character/up_idle/0.png").convert_alpha()
		self.animations['up_idle'][1] = pygame.image.load("import/graphics/character/up_idle/1.png").convert_alpha()
		self.animations['down_idle'][0] = pygame.image.load("import/graphics/character/down_idle/0.png").convert_alpha()
		self.animations['down_idle'][1] = pygame.image.load("import/graphics/character/down_idle/1.png").convert_alpha()
		self.animations['right_idle'][0] = pygame.image.load("import/graphics/character/right_idle/0.png").convert_alpha()
		self.animations['right_idle'][1] = pygame.image.load("import/graphics/character/right_idle/1.png").convert_alpha()
		self.animations['left_idle'][0] = pygame.image.load("import/graphics/character/left_idle/0.png").convert_alpha()
		self.animations['left_idle'][1] = pygame.image.load("import/graphics/character/left_idle/1.png").convert_alpha()

	def input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_UP]:
			self.direction.y = -1
			self.status = 'up'
		elif keys[pygame.K_DOWN]:
			self.direction.y = 1
			self.status = 'down'
		else:
			self.direction.y = 0

		if keys[pygame.K_RIGHT]:
			self.direction.x = 1
			self.status = 'right'
		elif keys[pygame.K_LEFT]:
			self.direction.x = -1
			self.status = 'left'
		else:
			self.direction.x = 0

	def move(self,dt):

		# normalizing a vector
		if self.direction.magnitude() > 0:
			self.direction = self.direction.normalize()

		# horizontal movement
		self.pos.x += self.direction.x * self.speed * dt
		self.hitbox.centerx = round(self.pos.x)
		self.rect.centerx = self.hitbox.centerx
		self.collision('horizontal')

		# vertical movement
		self.pos.y += self.direction.y * self.speed * dt
		self.hitbox.centery = round(self.pos.y)
		self.rect.centery = self.hitbox.centery
		self.collision('vertical')

	def animate(self, dt):
		self.frame_index +=4 *dt
		if self.frame_index >= len(self.animations[self.status]): self.frame_index = 0
		self.image = self.animations[self.status][int(self.frame_index)]
	def get_status(self):
		# if player is not moving then we will add _idle to the status
		if self.direction.magnitude() == 0:
			self.status = self.status.split('_')[0] + '_idle'

	def collision(self, direction):
		for sprite in self.collision_sprites.sprites():
			if hasattr(sprite, 'hitbox'):
				if sprite.hitbox.colliderect(self.hitbox):
					if direction == 'horizontal':
						if self.direction.x > 0:  # moving right
							self.hitbox.right = sprite.hitbox.left
						if self.direction.x < 0:  # moving left
							self.hitbox.left = sprite.hitbox.right
						self.rect.centerx = self.hitbox.centerx
						self.pos.x = self.hitbox.centerx

					if direction == 'vertical':
						if self.direction.y > 0:  # moving down
							self.hitbox.bottom = sprite.hitbox.top
						if self.direction.y < 0:  # moving up
							self.hitbox.top = sprite.hitbox.bottom
						self.rect.centery = self.hitbox.centery
						self.pos.y = self.hitbox.centery