class Entity:
    movable = False
    def __init__(self,pos,colour):
        self.colour = colour
        self.x, self.y = pos
    def get_pos(self):
        return self.x, self.y
    def collide_check(self,otherEntity):
        return NotImplementedError
    def resolve_collide(self,otherEntity):
        return NotImplementedError
    def update(self):
        pass
    def draw(self):
        pass