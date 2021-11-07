import pygame

class My_plane(pygame.sprite.Sprite):
	def __init__(self,bg_size):
		pygame.sprite.Sprite. __init__(self)
		self.image = pygame.image.load("plane.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.width,self.height = bg_size[0],bg_size[1]
		self.rect.left,self.rect.bottom=self.width-404,self.height
		self.crash_image = pygame.image.load("plane_crash.png").convert_alpha()
		self.speed = 5
		self.active=True
		self.mask=pygame.mask.from_surface(self.image)
	def move_up(self):
		if self.rect.top>0:
			self.rect.top-=self.speed
		else:
			self.rect.top=0
	def move_down(self):
		if self.rect.bottom<self.height:
			self.rect.bottom+=self.speed
		else:
			self.rect.bottom=self.height
	def move_left(self):
		if self.rect.left>0:
			self.rect.left-=self.speed
		else:
			self.rect.left=0
	def move_right(self):
		if self.rect.right<self.width:
			self.rect.right+=self.speed
		else:
			self.rect.right=self.width
			
