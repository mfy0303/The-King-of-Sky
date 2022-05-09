#####################################
#####################################
#####Coding by MFY0303 2021-11-07####
#####################################
#####################################
import pygame
import pickle
import my_plane
import enemy_plane
import bullet
import e_bullet
import easygui as gui
from pygame.locals import *
# global init
pygame.init()
size = width, height = 768,900
clock=pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("plane game")
bg_img = pygame.image.load("background.png").convert()
score_list_lv1=[]
score_list_lv2=[]
score_small_enemy=0
score_big_enemy=0
score_all=0
speed_bullet=0
speed_small_enemy=0
speed_big_enemy=0
score_font=pygame.font.SysFont("arial",36)
level_up_font=pygame.font.SysFont("arial",70)
me_object=my_plane.My_plane(size)
big_em_crash_object=enemy_plane.B_enemy(size)
small_em_crash_object=enemy_plane.S_enemy(size)
big_enemy_bullet_cycle=0
level_up=1000
level_flag=0
small_em_crash_delay=0
big_em_crash_delay=0

def read_s_file():
	try:
		print("try to read")
		pickle_file=open('sco','rb')
		print("read ok")
		global score_list_lv1
		score_list_lv1=pickle.load(pickle_file)
		pickle_file.close()
	except IOError:
		print("file not exist")
		pickle_file=open("sco",'wb')
		pickle_file.close()
def add_small_enemy(group1,group2,num):
	for i in range(num):
		s_em1=enemy_plane.S_enemy(size)
		group1.add(s_em1)
		group2.add(s_em1)
def add_big_enemy(group1,group2,num):
	for i in range(num):
		b_em1=enemy_plane.B_enemy(size)
		group1.add(b_em1)
		group2.add(b_em1)
def add_bullet(group1):
	bul=bullet.Bullet1(me_object.rect.midtop)
	group1.add(bul)
def add_e_bullet(group1):
	for each in big_enemy:
		e_bul=e_bullet.E_Bullet(each.rect.midtop,size)
		group1.add(e_bul)
bullets=pygame.sprite.Group()
e_bullets=pygame.sprite.Group()
enemy=pygame.sprite.Group()
small_enemy=pygame.sprite.Group()
add_small_enemy(small_enemy,enemy,5)
big_enemy=pygame.sprite.Group()
add_big_enemy(big_enemy,enemy,2)
running=True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running=False
		if event.type==KEYDOWN:
			if event.key==K_u:
				add_bullet(bullets)
	key_pressed=pygame.key.get_pressed()
	if key_pressed[K_w]:
		me_object.move_up()
	if key_pressed[K_s]:
		me_object.move_down()
	if key_pressed[K_a]:
		me_object.move_left()
	if key_pressed[K_d]:
		me_object.move_right()
	screen.blit(bg_img,(0,0))
	for e in bullets:
		if e.active:
			e.move()
			screen.blit(e.image,e.rect)
			e_hit_small = pygame.sprite.spritecollide(e,small_enemy,False,pygame.sprite.collide_mask)
			if e_hit_small:
				e.active=False
				score_small_enemy=score_small_enemy+10
				for each in e_hit_small:
					small_em_crash_delay=1
					small_em_crash_object = each
					each.active=False
			e_hit_big = pygame.sprite.spritecollide(e,big_enemy,False,pygame.sprite.collide_mask)
			if e_hit_big:
				e.active=False
				for each in e_hit_big:
					if each.blood > 0:
						each.blood=each.blood-1
					else:
						big_em_crash_delay=1
						big_em_crash_object=each
						each.active=False
						score_big_enemy=score_big_enemy+100
	score_all=score_small_enemy+score_big_enemy
	score_text=score_font.render("SCORE:%s"%str(score_all),True,(255,255,255))
	screen.blit(score_text,(10,5))
	l_text=level_up_font.render("LEVEL UP",True,(255,255,255))
	if score_all >= level_up:
		speed_bullet = 1
		speed_small_enemy=1
		speed_big_enemy=1
		level_flag=1
		level_up=level_up+1000
	if level_flag >= 1:
		screen.blit(l_text,(260,450))
		level_flag = level_flag + 1
		if level_flag == 100:
			level_flag=0
	for e in e_bullets:
		if e.active:
			e.move()
			screen.blit(e.image,e.rect)
		if speed_bullet == 1:
			speed_bullet=0
			each.speed=each.speed+0.5
	me_hit=pygame.sprite.spritecollide(me_object,e_bullets,False,pygame.sprite.collide_mask)
	if me_hit:
		me_object.active=False
		for e in me_hit:
			e.active=False
	e_down = pygame.sprite.spritecollide(me_object,enemy,False,pygame.sprite.collide_mask)
	if e_down:
		me_object.active=False
		for e in e_down:
			e.active=False
	for each in small_enemy:
		if each.active:
			each.move()
			screen.blit(each.image,each.rect)
		if speed_small_enemy == 1:
			speed_small_enemy=0
			each.speed=each.speed+0.5
	if small_em_crash_delay >= 1:
		screen.blit(small_em_crash_object.crash_image,small_em_crash_object.rect)
		small_em_crash_delay = small_em_crash_delay+1
		if small_em_crash_delay == 10:
			small_em_crash_object.reset()
			small_em_crash_object.active=True
			small_em_crash_delay=0
	for each in big_enemy:
		if each.active:
			each.move()
			if each.rect.bottom == each.height-450:
				big_enemy_bullet_cycle=big_enemy_bullet_cycle+1
				if big_enemy_bullet_cycle==400:
					add_e_bullet(e_bullets)
					big_enemy_bullet_cycle=0
			screen.blit(each.image,each.rect)
		if speed_big_enemy == 1:
			speed_big_enemy=0
			each.speed=each.speed+0.5
	if big_em_crash_delay >= 1:
		screen.blit(big_em_crash_object.crash_image,big_em_crash_object.rect)
		big_em_crash_delay = big_em_crash_delay+1
		if big_em_crash_delay == 10:
			big_enemy_bullet_cycle=0
			big_em_crash_object.reset()
			big_em_crash_object.active=True
			big_em_crash_object.blood=5
			big_em_crash_delay=0
	if me_object.active:
		screen.blit(me_object.image,me_object.rect)
	else:
		screen.blit(me_object.crash_image,me_object.rect)
		running=False
	pygame.display.flip()
	clock.tick(120)
read_s_file()
gui.msgbox("GAME OVER")
msg1="PLEASE INPUT YOUR NAME."
title1='input a name'
name=gui.enterbox(msg1,title1)
msg2='SCORE LIST'
title2='score list'
score_list_lv2.append(name)
score_list_lv2.append(score_all)
score_list_lv1.append(score_list_lv2)
score_list_lv1.sort(key=lambda x:x[1],reverse=True)
print(score_list_lv1)
gui.choicebox(msg2,title2,score_list_lv1)
print(score_list_lv1)
pickle_file=open("sco",'wb')
pickle.dump(score_list_lv1,pickle_file)
pickle_file.close()





