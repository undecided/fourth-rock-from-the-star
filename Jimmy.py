import random
import math

def jimmy_generate(max_width, max_height):
    x = random.randint(0, max_width)
    y = random.randint(0, max_height)
    return (x, y)

def jimmy_distance(you, jimmy):
    (you_x, you_y)     = you
    (jimmy_x, jimmy_y) = jimmy
    return math.hypot(jimmy_x - you_x, jimmy_y - you_y)

def jimmy_comment(distance):
    if distance < 5:
        return "They call me Josh too!"
    if distance < 10:
        return "Lucy in the sky with diamonds!"
    return "Come closer!"

