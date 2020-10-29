# Caroline Davis (cnd7cy)
import pygame
import gamebox
import random
from random import randint

camera = gamebox.Camera(800, 300)

# set up
# ----------------------------------------------------------------------------------------------------------------------

# variables
score = 0
health = 3
dash = -15
if score % 20 == 0 and score >= 20:  # allows for an accelerating level
    dash -= 10
drift = -20
gravity = 0
jump = 0
game_on = False

# music !!! if your computer can run .ogg files then try it out as a fifth element!
# pygame.mixer.init()  # from https://www.pygame.org/docs/ref/music.html
# pygame.mixer.music.load("Common Fight.ogg")  # from https://patrickdearteaga.com/chiptune-8-bit-retro/
# pygame.mixer.music.play(loops = -1)  # loops set to -1 will run indefinitely


# text
title = gamebox.from_text(400, 100, "welcome to macrophage inc.", 24, 'white')
description1 = gamebox.from_text(390, 130, "your goal. simple. even a cell can do it.", 24, 'white')
description2 = gamebox.from_text(390, 160, "eat the foreign bacteria (red). avoid the good bacteria (green). enjoy some glucose (purple).", 24, 'white')
credit = gamebox.from_text(390, 280, "ceo: cnd7cy", 24, 'white')
funFact = gamebox.from_text(380, 220, "", 24, 'white')


# environment
ground = gamebox.from_color(400, 300, "maroon", 1000, 20)
top = gamebox.from_color(400, 300, "maroon", 1000, 50)


# sprites
macrophage = gamebox.from_image(400, 250, 'macrophage.png')
macrophage.scale_by(0.08)

badBacteria = gamebox.from_image(700, 270, 'bad.png')
badBacteria.scale_by(0.05)

goodBacteria = gamebox.from_image(750, 270, 'good.png')
goodBacteria.scale_by(0.07)

glucose = gamebox.from_image(400, 150, 'glucose.png')
glucose.scale_by(0.05)


# health bar creation
health1 = gamebox.from_color(100, 50, 'pink', 30, 30)
health2 = gamebox.from_color(131, 50, 'pink', 30, 30)
health3 = gamebox.from_color(162, 50, 'pink', 30, 30)
healthBar = [health1, health2, health3]

#  ~~ logistics ~~
badBacteria.xspeed = dash
goodBacteria.xspeed = dash
badBacteria.yspeed = jump + gravity
goodBacteria.yspeed = jump + gravity
glucose.xspeed = drift
# ----------------------------------------------------------------------------------------------------------------------


def funFactProb():
    """funFactProb takes in the empty funFact string and through probability distribution, assigns funFact to a random
    fun fact that will be displayed on the start-up screen
    :param: funFact = string value of a fun fact from https://www.news-medical.net/
    :return: funFact = displayed on title sequence"""

    global funFact

    probValue = randint(0, 10)
    if probValue <= 2:
        funFact = gamebox.from_text(380, 210, "did you know that macrophages exist in all tissues?", 24, 'white')
    elif probValue <= 4:
        funFact = gamebox.from_text(380, 210, "did you know that macrophages can change their physiology?", 24, 'white')
    elif probValue <= 6:
        funFact = gamebox.from_text(380, 210, "did you know that macrophages are big white blood cells?", 24, 'white')
    elif probValue <= 8:
        funFact = gamebox.from_text(380, 210, "did you know that macrophages ingest target cells by phagocytosis?", 24, 'white')
    elif probValue <= 10:
        funFact = gamebox.from_text(380, 210, "did you know that macrophages are the body's first line of defense?", 24, 'white')
    return funFact


funFactProb()


def healthDraw():
    """healthDraw creates the health bar at the top of the gamebox
        :param: health1, health2, health3 = gamebox rectangular images to convey health to user
        :param: healthBar = list of health images for organization
        :param: health = int value of user's health that corresponds to the drawn health bar
        :return: does not return specific value, just constantly monitors the health and draws the bar accordingly"""

    global health1
    global health2
    global health3
    global healthBar
    global health
    if health == 3:
        camera.draw(health1)
        camera.draw(health2)
        camera.draw(health3)
    if health == 2:
        camera.draw(health1)
        camera.draw(health2)
    if health == 1:
        camera.draw(health1)


def spriteInteractions():
    """spriteInteractions sets the rules for each sprite in regards to the other sprites during gameplay
        :param: macrophage, badBacteria, goodBacteria, glucose = sprites that are used to establish gameplay
        :return: no return, establishes gamebox 'touching' rules for each sprite"""

    global score
    global health
    global game_on
    global macrophage
    global badBacteria
    global goodBacteria
    global glucose

    if macrophage.touches(badBacteria):
        badBacteria.x = 1000
        score += 1
    if macrophage.touches(goodBacteria):
        goodBacteria.x = 1100
        health -= 1
    if macrophage.touches(glucose):
        glucose.x = 2000
        if health < 3:
            health += 1
    if health == 0:
        macrophage.y = 260
        health = 3
        # pygame.mixer.music.rewind()    also un-comment this line if .ogg works!
        game_on = False


def tick(keys):
    """ tick runs the gameplay of macrophage inc.
    :param: keys: input of user's keyboard functions to allow for sprite movement in gameplay
    :return: no return, gameplay is continued through the amount of ticks specified by the gamebox.timer_loop """
    global game_on
    global score
    global health
    global macrophage
    global badBacteria
    global goodBacteria
    global dash
    global drift
    global jump
    global gravity

    if not game_on:
        if pygame.K_SPACE in keys:
            game_on = True
            score = 0
    if game_on:
        title.x = 1000
        description1.x = 2000
        description2.x = 2000
        credit.x = 2000
        funFact.x = 2000
        badBacteria.move_speed()
        goodBacteria.move_speed()
        glucose.move_speed()

        # allows the user to jump and enacts gravity
        if macrophage.touches(ground):
            macrophage.y = 272
            if pygame.K_UP in keys:
                macrophage.y -= 100
                gravity = 9.8
            else:
                gravity = 0
        else:
            macrophage.y -= gravity
            gravity -= 4

    # re-establishes the sprites onto the screen
    if badBacteria.x <= 0:
        badBacteria.x += 800 + random.randrange(0, 500)
    if goodBacteria.x <= 0:
        goodBacteria.x += 800 + random.randrange(0, 500)
    if glucose.x <= -500:
        glucose.x += 1500

    # accounts for the random chance that badBacteria and goodBacteria are placed on top of each other
    if badBacteria.touches(goodBacteria):
        badBacteria.x += (goodBacteria.x + 50)

    scoreBoard = gamebox.from_text(camera.left + 70, 20, "score: " + str(score), 24, 'white')

    # camera functions
    camera.clear("black")
    camera.draw(macrophage)
    camera.draw(badBacteria)
    camera.draw(goodBacteria)
    camera.draw(glucose)
    camera.draw(title)
    camera.draw(description1)
    camera.draw(description2)
    camera.draw(funFact)
    camera.draw(credit)
    healthDraw()
    camera.draw(ground)
    camera.draw(scoreBoard)

    camera.display()
    spriteInteractions()


gamebox.timer_loop(30, tick)  # the long-awaited timer_loop function
