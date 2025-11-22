import pgzrun
from circle import MovingCircle, OpenCircle, HollowCircle
from scene import Scene
from utils import *
import numpy as np
import pygame
import random
from rectangle import Rectangle
from butterfly import *
from duplicating import *

WIDTH = 600
HEIGHT = 600

scene = Scene((0,0,0),0.05,WIDTH,HEIGHT)

Duplicating(scene)

# butterfly_effect(scene, 100,(WIDTH/2+100,HEIGHT/2),pygame.Color((255,0,0)))

test = Rectangle((WIDTH/2,HEIGHT/2),(0,0,0),width=100,height=100)
# scene.add(test)


def update():
    scene.update()

def draw():
    scene.draw(screen)

pgzrun.go()


# bug: when the gap of an open circle moves across the origin, the collision detection doesn't work properly (fixed)
# TODO: MovingCircle-MovingCircle collision and collision resolution (elastic circle collision)
#       squares and rectangles
#       classes of moving circles (fibonacci, sword, unarmed etc)
#       delta time
#       implement numpy
#       sparks and sound effects on collisions
#       collidable vs movable
#       optimisations: only check for collisions that are close. use numpy and vectorisation -> compute all resultant velocities and apply them all at once