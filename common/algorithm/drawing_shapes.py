import numpy as np
import math
import cv2

def draw_ellipse(points):
    rrt = cv2.fitEllipse(points)
    cx, cy = rrt[0][0], rrt[0][1]
    rx, ry = rrt[1][0], rrt[1][1]
    listofpoints = []
    rad = rrt[2] * 3.14 / 180
    for i in np.arange(0, 2 * math.pi, 0.1):
        x = cx - (ry * 0.5 * math.sin(i)) * math.sin(rad) + (rx * 0.5 * math.cos(i)) * math.cos(rad)
        y = cy + (rx * 0.5 * math.cos(i)) * math.sin(rad) + (ry * 0.5 * math.sin(i)) * math.cos(rad)
        listofpoints.append([x, y])

    return listofpoints

def draw_minRect(points):
    rect = cv2.minAreaRect(points)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    return box

def draw_boundingRect(points):
    brect = cv2.boundingRect(points)

    return brect

def draw_circle(points):
    (x, y), radius = cv2.minEnclosingCircle(points)
    circle_points = []
    for i in np.arange(0, 2 * math.pi, 0.1):
        #ang = 2 * math.pi * i
        circle_points.append([math.sin(i) * radius + x, math.cos(i) * radius + y])

    return circle_points