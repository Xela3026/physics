from entity import Entity
import pygame
class Rectangle(Entity):
    def __init__(self,*args,width=0,height=0,affectedByGravity=False,**kwargs):
        # pos is top left
        self.width = width
        self.height = height
        self.affectedByGravity = affectedByGravity
        super().__init__(*args, **kwargs)
    def rect(self):
        return pygame.Rect(*self.pos(),self.width,self.height)
    def draw(self,screen):
        pygame.draw.rect(screen.surface,self.colour,self.rect())
    