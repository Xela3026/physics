from circle import MovingCircle, OpenCircle, HollowCircle
from utils import *
import pygame


def butterfly_effect(scene,num_balls,start_pos,start_colour):
    boundary = HollowCircle((scene.width/2,scene.height/2),(0,0,0),radius=300)
    scene.add(boundary)
    colour_change = 360 / num_balls
    total_diff = 1
    increment = total_diff / num_balls
    for i in range(num_balls):
        x,y = start_pos
        y += increment * i
        colour = increment_colour(start_colour,colour_change * i)
        ball = MovingCircle((x,y),colour,radius=10)
        scene.add(ball)