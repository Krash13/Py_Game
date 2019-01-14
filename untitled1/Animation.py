import pygame


class Animation:
    def __init__(self, name, n_cadrs):
        self.n = n_cadrs
        self.cadrs = []
        temp = pygame.image.load(name).convert_alpha()
        for i in range(self.n):
            self.cadrs.append(temp.subsurface(i * 96, 0, 96, 96))
        self.number = 0
        self.cadr = self.cadrs[self.number]
    def update(self):
        self.number += 1
        if self.number == self.n:
            self.number = 0
            self.cadr = self.cadrs[self.number]
            return bool(False)
        self.cadr = self.cadrs[self.number]
        return bool(True)
