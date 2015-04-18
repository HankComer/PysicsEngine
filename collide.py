from data_classes import *




def resolveCollision(a, b):
    #relative velocity
    rv = b.velocity - a.velocity

    #relative velocity along normal
    velAlongNormal = rv * normal

    #do not resolve if they are heading away from eachother
    if (velAlongNormal > 0):
        return
    e = min(a.restitution, b.restitution)

    #impulse scalar
    j = -(1.0+e) * velAlongNormal
    j /= 1.0 / a.mass + 1.0 / b.mass

    impulse = Point(j * normal.x, j * normal.y)
    a.velocity -= impulse / a.mass
    b.velocity += impulse / b.mass
