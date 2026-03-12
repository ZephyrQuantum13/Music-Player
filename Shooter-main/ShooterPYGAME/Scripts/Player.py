from BasePerson import BaseSprite
from pygame import *
from coonfig import *
class Player(BaseSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
            print("x:" ,self.rect.x)
        if keys_pressed[K_RIGHT] and self.rect.x < win_WIDTH - self.rect.width:
            self.rect.x += self.speed
            print("x:" ,self.rect.x)
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
            print("y:" ,self.rect.y)
        if keys_pressed[K_DOWN] and self.rect.y < win_HEIGHT - self.rect.height:
            self.rect.y += self.speed
            print("y:" ,self.rect.y)

    def fire(self):
        pass