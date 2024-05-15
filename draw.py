import turtle
from utils import *
import reeds_shepp as rs
import random as rd

SCALE = 40

def scale(x):
    if type(x) is tuple or type(x) is list:
        return [p * SCALE for p in x]
    return x * SCALE

def unscale(x):
    if type(x) is tuple or type(x) is list:
        return [p / SCALE for p in x]
    return x / SCALE

def vec(bob):
    bob.down()
    bob.pensize(3)
    bob.forward(scale(1.2))
    bob.right(25)
    bob.backward(scale(.4))
    bob.forward(scale(.4))
    bob.left(50)
    bob.backward(scale(.4))
    bob.forward(scale(.4))
    bob.right(25)
    bob.pensize(1)
    bob.up()

def goto(bob, pos, scale_pos=True):
    bob.up()
    if scale_pos:
        bob.setpos(scale(pos[:2]))
    else:
        bob.setpos(pos[:2])
    bob.setheading(pos[2])
    bob.down()

def draw_path(bob, path):
    for e in path:
        gear = 1 if e.gear == rs.Gear.FORWARD else -1
        if e.steering == rs.Steering.LEFT:
            bob.circle(scale(1), gear * rad2deg(e.param))
        elif e.steering == rs.Steering.RIGHT:
            bob.circle(- scale(1), gear * rad2deg(e.param))
        elif e.steering == rs.Steering.STRAIGHT:
            bob.forward(gear * scale(e.param))

def set_random_pencolor(bob):
    r, g, b = 1, 1, 1
    while r + g + b > 2.5:
        r, g, b = rd.uniform(0, 1), rd.uniform(0, 1), rd.uniform(0, 1)
    bob.pencolor(r, g, b)
