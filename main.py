import pgzrun
from circle import MovingCircle, OpenCircle, HollowCircle
from scene import Scene
import numpy as np

WIDTH = 800
HEIGHT = 800
A = MovingCircle((WIDTH/2 + 100,HEIGHT/2),(255,0,0),radius=30)
B = OpenCircle((WIDTH/2,HEIGHT/2),(0,0,0),radius=300,gap=(np.pi/3,2 * np.pi/3),angular_vel=0.01)
C = HollowCircle((WIDTH/2,HEIGHT/2),(0,0,0),radius=300)
scene = Scene((255,255,255),0.1)
scene.add(A)
scene.add(B)

def update():
    scene.update()

def draw():
    scene.draw(screen)

pgzrun.go()