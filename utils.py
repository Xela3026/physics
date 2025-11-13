import numpy as np
import pygame
def normalise(angle):
    two_pi = 2 * np.pi
    normalized_angle = angle % two_pi
    if normalized_angle < 0:
        normalized_angle += two_pi
    return normalized_angle

def cartesian_to_polar(p):
    x, y = p
    r = np.sqrt(x**2+y**2)
    if x == 0:
        return r, normalise(np.sign(y) * np.pi / 2)
    theta = -np.arctan2(y,x)
    return r, normalise(theta)

def progress_colour(colour,change):
    h, s, v, a = colour.hsva
    colour.hsva = (h + change) % 361, s, v, a
