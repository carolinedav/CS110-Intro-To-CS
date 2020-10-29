# Caroline Davis (cnd7cy)
# Maia Jenckes (mcj9ax) absolutely SAVED my life for this assignment by helping me with pretty much every issue I had
# so massive thanks to her :)
import pygame
import gamebox
import random

heightCactus = random.randrange(20, 60)


score = 0
camera = gamebox.Camera(800, 300)

ground = gamebox.from_color(400, 300, 'green', 1000, 20)
dino = gamebox.from_color(400, 260, 'red', 40, 80)
cactus1 = gamebox.from_color(700, 280, 'pink', 30, heightCactus)
cactus2 = gamebox.from_color(700, 280, 'pink', 30, heightCactus)
sun = gamebox.from_color(550, 80, 'yellow', 50, 20)


drift = -8
dash = -15
score = 0
game_on = False

ticker = 0

jump = 0
gravity = 0
cactus1.xspeed = dash
cactus2.xspeed = dash
cactus1.yspeed = jump + gravity
cactus2.yspeed = jump + gravity
sun.xspeed = drift


def tick(keys):
    global game_on
    global score
    global dino
    global cactus1
    global cactus2
    global sun
    global gravity
    global jump
    global dash
    global heightCactus

    height = random.randrange(20, 60)

    if not game_on:
        if pygame.K_SPACE in keys:
            game_on = True
            score = 0
    if game_on:
        cactus1.move_speed()
        cactus2.move_speed()
        sun.move_speed()

        if dino.touches(ground):
            dino.y = 260
            if pygame.K_UP in keys:
                dino.y -= 100
                gravity = 9.8
            else:
                gravity = 0
        else:
            dino.y -= gravity
            gravity -= 3.5
    if cactus1.x <= 0:
        cactus1.size = [30, height]
        cactus1.x += 800 + random.randrange(0, 500)
    if cactus2.x <= 0:
        cactus2.size = [30, height]
        randomPos2 = cactus1.x + random.randrange(500, 700)
        cactus2.x += randomPos2
    if sun.x <= -500:
        sun.x += 1500

    scoreBoard = gamebox.from_text(camera.left + 70, 20, "score: " + str(score), 24, 'black')

    camera.clear('light blue')
    camera.draw(dino)
    camera.draw(cactus1)
    camera.draw(cactus2)
    camera.draw(sun)
    camera.draw(ground)
    camera.draw(scoreBoard)
    camera.display()

    if game_on:
        score += 1

    if dino.touches(cactus1):
        dino.y = 260
        cactus1.x = 770
        cactus1.y = 300 - (heightCactus / 2)
        cactus2.x = 770
        cactus2.y = 300 - (heightCactus / 2)
        game_on = False
    if dino.touches(cactus2):
        cactus1.x = 770
        cactus1.y = 300 - (heightCactus / 2)
        cactus2.x = 770
        cactus2.y = 300 - (heightCactus / 2)
        dino.y = 300 - 50
        game_on = False

gamebox.timer_loop(30, tick)
