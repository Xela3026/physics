from utils import *
import numpy as np

class Vec:
    def __init__(self,start,end):
        self.x, self.y = start, end
        self.r, self.angle = cartesian_to_polar((self.x, self.y))
    def to_polar(self):
        return self.r, self.angle
    def distance_to(self,vec):
        x2 = (self.x - vec.x)**2
        y2 = (self.y - vec.y)**2
        return np.sqrt(x2 + y2)
    def is_between(self,a1,a2):
        angle = normalise(self.angle)
        start = normalise(a1)
        end = normalise(a2)
    def normalise(self):
        return 1 / self.r * self
        return start > angle and angle > end
    def dot(self,vec):
        return self.x * vec.x + self.y * vec.y
    def proj_onto(self,vec):
        dot = self.dot(vec)
        return (dot / vec.r**2) * vec
    def __iter__(self):
        yield self.x
        yield self.y
    def __repr__(self):
        return f"Vec({self.x},{self.y})"
    def __str__(self):
        return f"({self.x},{self.y})"
    def __add__(self,vec):
        return Vec(self.x + vec.x, self.y + vec.y)
    def __rmul__(self,k):
        return Vec(k * self.x, k * self.y)
    def __sub__(self,vec):
        return Vec(self.x - vec.x, self.y - vec.y)
    def __neg__(self):
        return Vec(-self.x,-self.y)

if __name__ == "__main__":
    a = Vec(1,1)
    b = Vec(2,3)
    c = a + b
    d = a - b
    print(d)
    print(d.to_polar())
    print(a.distance_to(b))
    print(2 * d)
    print(a.normalise())

# could generalise to an n-dimensional vector