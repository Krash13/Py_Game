import pygame
from Animation import *
from Player import *
from Constans import *
pygame.time.set_timer(pygame.USEREVENT, 200)
FPS=60
clock=pygame.time.Clock()
pygame.init()
sc=pygame.display.set_mode((1000,500))

but=pygame.Surface((50,50))
but.fill((255,0,0))
rect1=but.get_rect()
rect1.x=50
rect1.y=200
but1=pygame.Surface((50,50))
but1.fill((0,255,0))
rect2=but.get_rect()
rect2.x=100
rect2.y=200
but2=pygame.Surface((50,50))
but2.fill((0,0,255))
rect3=but.get_rect()
rect3.x=150
rect3.y=200


animations=[]
animations.append(Animation('picture/looking.png',12))
animations.append(Animation('picture/attack.png',12))
animations.append(Animation('picture/run.png',8))
animations.append(Animation('picture/talking.png',8))
player1=Player(animations,50,50)

GAME=True
sc.blit(player1.image,player1.rect)
sc.blit(but,rect1)
sc.blit(but1,rect2)
sc.blit(but2,rect3)
pygame.display.update()
while GAME:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            GAME=False
        elif i.type==pygame.USEREVENT:
            player1.animated()
        elif i.type==pygame.MOUSEBUTTONDOWN:
            if rect1.collidepoint(i.pos):
                player1.state=ATTACK
            elif rect2.collidepoint(i.pos):
                player1.state =RUN
            elif rect3.collidepoint(i.pos):
                player1.state = TALKING
        sc.fill((255,255,255))
        sc.blit(player1.image, player1.rect)
        sc.blit(but, rect1)
        sc.blit(but1, rect2)
        sc.blit(but2, rect3)
        pygame.display.update()
        clock.tick(FPS)

