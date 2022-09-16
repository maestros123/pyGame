from map import Map
import time
import os
from helicopter import Helicopter 
from pynput import keyboard

UPDATE = 100
MAP_W, MAP_H = 20, 20

tmp = Map(MAP_W, MAP_H)
tmp.generate_forest(7, 10)
tmp.generate_river(25)
tmp.generate_fire()
tmp.generate_fire()
tmp.generate_fire()


helico = Helicopter(MAP_W, MAP_H)

MOVES = {'w': (-1, 0), 'd': (0, 1) , 's': (1, 0), 'a': (0, -1) }


def on_release(key):
    global helico
    c = key.char
    
    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        helico.move(dx, dy)

listener = keyboard.Listener(
    on_press=None,
    on_release=on_release)
listener.start()


tick = 1
while True:
    os.system('CLS')
    print('Кадр', tick)
    tmp.print_map(helico)
    tick += 1
    time.sleep(0.00005)
    if (tick % UPDATE == 0):
        # tmp.generate_tree()
        tmp.update_fire()