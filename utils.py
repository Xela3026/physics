import numpy as np

def normalize(angle):
    two_pi = 2 * np.pi
    normalized_angle = angle % two_pi
    if normalized_angle < 0:
        normalized_angle += two_pi
    return normalized_angle

def cartesian_to_polar(p):
    x, y = p
    r = np.sqrt(x**2+y**2)
    if x == 0:
        return r, normalize(np.sign(y) * np.pi / 2)
    theta = -np.arctan2(y,x)
    return r, normalize(theta)
