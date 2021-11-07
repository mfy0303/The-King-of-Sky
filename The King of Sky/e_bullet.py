import pygame

class E_Bullet(pygame.sprite.Sprite):
	init_position = 0,0
	def __init__(self,position,bg_size):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("bul.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.left,self.rect.top = position
		self.init_position = position
		self.width,self.height = bg_size[0],bg_size[1]
		self.speed=2
		self.active=True
		self.mask=pygame.mask.from_surface(self.image)
	def move(self):
		self.rect.bottom+=self.speed
		if self.rect.bottom > self.height+100:
			self.active=False
	def reset(self):
		self.rect.left,self.rect.top = self.init_position
		self.active=True
			

	
		
