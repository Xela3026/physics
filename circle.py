from entity import Entity
from vec import Vec
import pygame
from utils import *
import numpy as np
class Circle(Entity):
    def __init__(self,*args,radius=0,**kwargs):
        self.radius = radius
        super().__init__(*args, **kwargs)

    def draw(self,screen):
        screen.draw.circle(self.pos(),self.radius,self.colour)
    def __repr__(self):
        return f"Circle({self.pos()},{self.colour},{self.radius})"
    
class MovingCircle(Circle):
    movable = True
    _ball_collisions = False
    def __init__(self,*args,initial_vel=(0,0),affectedByGravity=True,collision_func=lambda self: None,escape_func=lambda self: None,**kwargs):
        super().__init__(*args, **kwargs)
        self.xvel, self.yvel = initial_vel
        self.affectedByGravity = affectedByGravity
        self.collision_func = collision_func
        self.escape_func = escape_func
    def update(self,gravity=0):
        if self.affectedByGravity:
            self.yvel += gravity
        self.y += self.yvel
        self.x += self.xvel
        progress_colour(self.colour,0.25)
    def vel(self):
        return Vec(self.xvel, self.yvel)
    def collide_check(self,otherEntity):
        if isinstance(otherEntity,Circle):
            r1 = self.radius
            r2 = otherEntity.radius
            p1 = self.pos() # where will it be in the future
            p2 = otherEntity.pos()
            dist = p1.distance_to(p2)
            if isinstance(otherEntity,MovingCircle) and self._ball_collisions:
                return dist < (r1 + r2)
            elif isinstance(otherEntity,HollowCircle):
                if dist < r2: # inside circle (can remove this condition to keep them in circle for much longer)
                    future_dist = (p1 + self.vel()).distance_to(p2)
                    if future_dist + r1 < r2: # not colliding
                        return False
                    if not isinstance(otherEntity,OpenCircle):
                        return True
                    start, end = otherEntity.get_gap()
                    if (p1-p2).is_between(start,end):
                        self.escape_func(self)
                        return False
                    return True
                # outside circle
                return dist + r1 < r2
    def resolve_collide(self,otherEntity):
        if isinstance(otherEntity,HollowCircle):
            incidence = self.vel()
            p1 = self.pos()
            p2 = otherEntity.pos()
            # find vector between circle centres
            # AB = b - a
            reflection_line = p2 - p1
            projection = incidence.proj_onto(reflection_line)
            self.xvel, self.yvel = -1.01*(2 * projection - incidence)
            dist = p1.distance_to(p2)
            overlap = dist + self.radius - otherEntity.radius
            if overlap > 0:
                direction = reflection_line.normalise()
                correction = overlap * direction
                self.x += correction.x
                self.y += correction.y
            self.collision_func(self)
        return NotImplementedError
    def draw(self,screen):
        screen.draw.filled_circle(self.pos(),self.radius,self.colour)
        screen.draw.circle(self.pos(),self.radius,(255,255,255))
    def __repr__(self):
        return f"MovingCircle({self.pos()},{self.colour},{self.radius},{self.vel()})"
            
class HollowCircle(Circle):
    affectedByGravity = False
    def __repr__(self):
        return f"HollowCircle({self.pos()},{self.colour},{self.radius})"

class OpenCircle(HollowCircle):
    def __init__(self,*args,start_gap=0,gap_size=0,angular_vel=0,**kwargs):
        self._start_gap = start_gap
        self._gap_size = gap_size
        self._angular_vel = angular_vel
        super().__init__(*args,**kwargs)
    def get_gap(self):
        # reverse to get the full major arc instead of minor arc
        return self._start_gap + self._gap_size, self._start_gap
    def get_angular_vel(self):
        return self._angular_vel
    def move_gap(self,angle):
        self._start_gap = normalise(self._start_gap+angle)
    def draw(self,screen):
        r = self.radius
        top_left = (self.x - r, self.y - r)
        dimensions = (r*2,r*2)
        bounding_box = pygame.Rect(top_left,dimensions)
        pygame.draw.arc(screen.surface,self.colour,bounding_box,*self.get_gap())
    def update(self):
        self.move_gap(self.get_angular_vel())
        