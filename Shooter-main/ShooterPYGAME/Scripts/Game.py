from pygame import *
import sys
from Player import Player
from random import *
from coonfig import *
from Emeny import Enemy

mixer.init()
clock = time.Clock()

window = display.set_mode((win_WIDTH, win_HEIGHT))
display.set_caption("Шутер")
background = transform.scale(image.load(r"..\content\img\phon.jpg"), (win_WIDTH, win_HEIGHT))

mixer.music.load(r"..\content\sounds\Orbital Slipstream.mp3")
mixer.music.play()

player = Player(r"..\content\img\ship.jpg", 100, 100, 5)
monsters = sprite.Group()

for i in range(1,6):
    monster = Enemy(r"..\content\img\NLO.jpg",  randint(80, win_WIDTH - 80), 0, speed)
    monsters.add(monster)
while True:
    
    clock.tick(FPS)
    window.blit(background, (0, 0))
    player.reset(window)
    player.update()
    monsters.update()
    monsters.draw(window)
    for e in event.get():
        if e.type == QUIT:
            sys.exit()

    display.update()


