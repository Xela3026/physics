from entity import Entity
class Rectangle(Entity):
    def __init__(self,pos,colour):
        self.x, self.y = pos
        self._colour = colour
    