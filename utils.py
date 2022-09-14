from random import randint as rand
import re

def randbool(r, mxr):
    t = rand(0, mxr)
    return (t <= r)

def randcell(w, h):
    tw = rand(0, w)
    th = rand(0, h)
    return (tw, th)

def randcell2(x, y):
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # Для перемещения по координатам (0-вверх, 1-право, 2-низ, 3-лево)
    dir = rand(0, 3)
    dx, dy = moves[dir][0], moves[dir][1]
    return(x + dx, y + dy)
