import pygame
from random import *

class S_enemy(pygame.sprite.Sprite):
	def __init__(self,bg_size):
		pygame.sprite.Sprite.__init__(self)
		self.crash_image = pygame.image.load("em_plane_crash.png").convert_alpha()
		self.image = pygame.image.load("em_plane.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.width,self.height = bg_size[0],bg_size[1]
		self.speed=1
		self.rect.left,self.rect.bottom = randint(0,self.width-self.rect.width),\
		randint(-1 * self.height,0)
		self.active=True
		self.mask=pygame.mask.from_surface(self.image)
	def reset(self):
		self.rect.left,self.rect.bottom = randint(0,self.width-self.rect.width),\
		randint(-1 * self.height,0)
	def move(self):
		if self.rect.top<self.height:
			self.rect.top += self.speed
		else:
			self.reset()
class B_enemy(pygame.sprite.Sprite):
	f=0
	blood=5
	def __init__(self,bg_size):
		pygame.sprite.Sprite.__init__(self)
		self.crash_image = pygame.image.load("b_enemy_crash.png").convert_alpha()
		self.image = pygame.image.load("B_enemy.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.width,self.height = bg_size[0],bg_size[1]
		self.speed=1
		self.rect.left,self.rect.bottom = randint(0,self.width-self.rect.width),\
		randint(-1 * self.height,0)
		self.active=True
		self.mask=pygame.mask.from_surface(self.image)
	def reset(self):
		self.rect.left,self.rect.bottom = randint(0,self.width-self.rect.width),\
		randint(-1 * self.height,0)
	def move(self):
		if self.rect.bottom < self.height-450:
			self.rect.top += self.speed
		else:
			if self.rect.left>0 and self.rect.right<self.width and self.f==0:
				self.rect.left -= self.speed
			if self.rect.left>0 and self.rect.right<self.width and self.f==1:
				self.rect.right += self.speed
			if self.rect.left<=0:
				self.f=1
				self.rect.right += self.speed
			if self.rect.right>=self.width:
				self.f=0
				self.rect.left -= self.speed
		
			
		
