from vec import Vec
import pygame
class Entity:
    movable = False
    collidable = False
    def __init__(self,pos,colour):
        self.colour = pygame.Color(colour)
        self.x, self.y = pos
    def pos(self):
        return Vec(self.x,self.y)
    def collide_check(self,otherEntity):
        return NotImplementedError
    def resolve_collide(self,otherEntity):
        return NotImplementedError
    def update(self):
        pass
    def draw(self):
        pass