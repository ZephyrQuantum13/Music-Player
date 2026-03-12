from BasePerson import BaseSprite
import pygame
from coonfig import *

from random import *
lost = 0
class Enemy(BaseSprite):
    def update(self):
        self.rect.y += randint(1, 100)
        global lost 
        
        if self.rect.y > 500:
            self.rect.y = 0

            self.rect.x = randint(80, win_WIDTH - 80)
            
            lost = lost + 1
            print(lost)