import pygame
from Animation import *
from Constans import *
class Player(pygame.sprite.Sprite):
    def __init__(self,animations,x,y):
        self.animations=animations
        self.state=DEAFAULT
        self.image=animations[self.state].cadr
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def animated(self):
        if not self.animations[self.state].update():
            self.state=DEAFAULT
        self.image = self.animations[self.state].cadr
