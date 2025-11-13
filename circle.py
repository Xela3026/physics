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
    def __init__(self,*args,initial_vel=(0,0),affectedByGravity=True,**kwargs):
        super().__init__(*args, **kwargs)
        self.xvel, self.yvel = initial_vel
        self.affectedByGravity = affectedByGravity
    def update(self,gravity=0):
        if self.affectedByGravity:
            self.yvel += gravity
        self.y += self.yvel
        self.x += self.xvel
    def vel(self):
        return Vec(self.xvel, self.yvel)
    def collide_check(self,otherEntity):
        r1 = self.radius
        r2 = otherEntity.radius
        p1 = self.pos()
        p2 = otherEntity.pos()
        dist = p1.distance_to(p2)
        # should also try future detection/prediction
        if isinstance(otherEntity,MovingCircle):
            return dist < (r1 + r2)
        elif isinstance(otherEntity,HollowCircle):
            if dist < r2: # inside circle
                if dist + r1 < r2: # not colliding
                    return False
                if not isinstance(otherEntity,OpenCircle):
                    return True
                start, end = otherEntity.get_gap()
                return not ((p1-p2).is_between(start,end))
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
            self.xvel, self.yvel = -(2 * projection - incidence)
    def __repr__(self):
        return f"MovingCircle({self.pos()},{self.colour},{self.radius},{self.vel()})"
            
class HollowCircle(Circle):
    affectedByGravity = False
    def __repr__(self):
        return f"HollowCircle({self.pos()},{self.colour},{self.radius})"

class OpenCircle(HollowCircle):
    def __init__(self,*args,gap=(0,0),angular_vel=0,**kwargs):
        self._start_gap, self._end_gap = gap[0], gap[1] - 2 * np.pi
        self._angular_vel = angular_vel
        super().__init__(*args,**kwargs)
    def get_gap(self):
        # reverse to get the full major arc instead of minor arc
        return self._end_gap, self._start_gap
    def get_angular_vel(self):
        return self._angular_vel
    def move_gap(self,angle):
        self._end_gap += angle
        self._start_gap += angle
    def draw(self,screen):
        r = self.radius
        top_left = (self.x - r, self.y - r)
        dimensions = (r*2,r*2)
        bounding_box = pygame.Rect(top_left,dimensions)
        pygame.draw.arc(screen.surface,self.colour,bounding_box,*self.get_gap())
    def update(self):
        self.move_gap(self.get_angular_vel())
        