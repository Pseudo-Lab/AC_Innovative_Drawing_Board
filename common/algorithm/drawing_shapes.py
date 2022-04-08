import numpy as np
import math

def draw_ellipse(ecenter, esize, erotation):
    cx, cy = ecenter[0], ecenter[1]
    rx, ry = esize[0], esize[1]
    listofpoints = []
    rad = erotation * 3.14 / 180
    for i in np.arange(0, 2 * math.pi, 0.1):
        x = cx - (ry * 0.5 * math.sin(i)) * math.sin(rad) + (rx * 0.5 * math.cos(i)) * math.cos(rad)
        y = cy + (rx * 0.5 * math.cos(i)) * math.sin(rad) + (ry * 0.5 * math.sin(i)) * math.cos(rad)
        listofpoints.append([x, y])

    return listofpoints