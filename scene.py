class Scene:
    def __init__(self,bg_colour,gravity=0):
        self.gravity = gravity
        self._objects = []
    def add(self,obj):
        self._objects.append(obj)
    def remove(self,obj):
        self._objects.remove(obj)
    def draw(self,screen):
        screen.fill((255,255,255))
        for obj in self._objects:
            obj.draw(screen)
    def update(self):
        # check if anything collides
        for obj1 in self._objects:
            if obj1.movable:
                for obj2 in self._objects:
                    if obj2.movable or obj1 == obj2: # in future might want a separate "collisions" attribute to check
                        continue
                    if obj1.collide_check(obj2):
                        obj1.resolve_collide(obj2)
            if obj1.affectedByGravity:
                obj1.update(self.gravity)
            obj1.update()