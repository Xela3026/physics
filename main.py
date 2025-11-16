import pgzrun
from circle import MovingCircle, OpenCircle, HollowCircle
from scene import Scene
from utils import *
import numpy as np
import pygame
import random

WIDTH = 800
HEIGHT = 800

def grow(entity):
    entity.radius += 2

def get_ball_vel(speed):
    return generate_random_vel(-speed,speed)

def new_circle():
    vel1 = get_ball_vel(2)
    vel2 = get_ball_vel(2)
    scene.add(MovingCircle((WIDTH/2,HEIGHT/2),(255,0,0),radius=5,escape_func=new_circle,initial_vel=vel1))
    scene.add(MovingCircle((WIDTH/2,HEIGHT/2),(255,0,0),radius=5,escape_func=new_circle,initial_vel=vel2))

# need to optimise now. use numpy probs

vel = get_ball_vel(2)
A = MovingCircle((WIDTH/2,HEIGHT/2),(255,0,0),radius=5,escape_func=new_circle,initial_vel=vel)
D = MovingCircle((WIDTH/2 - 100,HEIGHT/2),(0,255,0),radius=30)
E = MovingCircle((WIDTH/2 + 100,HEIGHT/2 + 100),(0,0,255),radius=30)
B = OpenCircle((WIDTH/2,HEIGHT/2),(0,0,0),radius=300,gap=(np.pi/3,2 * np.pi/3),angular_vel=0.01)
C = HollowCircle((WIDTH/2,HEIGHT/2),(255,255,255),radius=300)
scene = Scene((255,255,255),0.05)
scene.add(A)
# scene.add(D)
# scene.add(E)
scene.add(B)

def update():
    scene.update()

def draw():
    scene.draw(screen)

pgzrun.go()