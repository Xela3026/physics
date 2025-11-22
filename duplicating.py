from utils import *
from circle import MovingCircle, OpenCircle


class Duplicating:
    def __init__(self,scene,ball_size=25):
        vel = get_ball_vel(2)
        self.radius = ball_size
        A = MovingCircle((scene.width/2,scene.height/2),(255,0,0),radius=self.radius,escape_func=self.new_circle,initial_vel=vel,collision_func=grow)
        B = OpenCircle((scene.width/2,scene.height/2),(255,255,255),radius=300,start_gap=0,gap_size=np.pi/3,angular_vel=0.01)
        scene.add(A)
        scene.add(B)
        self.scene = scene
    def new_circle(self,entity):
        vel1 = get_ball_vel(2)
        vel2 = get_ball_vel(2)
        self.scene.add(MovingCircle((self.scene.width/2,self.scene.height/2),(255,0,0),radius=self.radius,escape_func=self.new_circle,initial_vel=vel1,collision_func=grow))
        self.scene.add(MovingCircle((self.scene.width/2,self.scene.height/2),(255,0,0),radius=self.radius,escape_func=self.new_circle,initial_vel=vel2,collision_func=grow))
        self.scene.remove(entity)

def grow(entity):
    entity.radius += 2

def get_ball_vel(speed):
    return generate_random_vel(-speed,speed)
    

