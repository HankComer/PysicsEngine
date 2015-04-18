
from math import sqrt



class Point(object):
    __slots__ = ['x', 'y']
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y



def distance(a, b):
    return sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)


class AABB(object):
    __slots__ = ['min', 'max']
    def __init__(self, small, largs):
        self.min = small
        self.max = large
        
def collide(a, b):
    if (a.max.y < b.min.x or a.min.x > b.max.x):
        return False
    if (a.max.y < b.min.y or a.min.y > b.max.y):
        return False
    return True


class Circle(object):
    __slots__ = ['radius', 'position']
    def __init__(self, radius, position):
        self.radius = radius
        self.position = position


def fastCircleCollide(a, b):
    r = a.radius + b.radius
    r *= r
    return r < (((a.position.x + b.position.x) ** 2) + ((a.position.y + b.position.y) ** 2))
