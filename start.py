#!/usr/bin/env python3

import random

from adventurelib import *

from RockMap import RockMap
import Jimmy
import Terrain

jimmy_loc = Jimmy.jimmy_generate(9,9)

inventory = []

map = RockMap()

def print_status():
    print("Status")
    terrain_number = map.get_terrain()
    pos = map.position
    jimmy_distance = Jimmy.jimmy_distance((pos[0], pos[1]), jimmy_loc)
    print("Jimmy says: %s" % Jimmy.jimmy_comment(jimmy_distance))
    print("Terrain: %s " % Terrain.get_description(terrain_number))

def walk(x, y):
    map.move_player(x,y)
    print('Walking up %s and right %s...' % (x, y))

@when('walk north')
def walk_north():
    print_status()
    walk(0, 1)

@when('walk east')
def walk_east():
    walk(1, 0)

@when('walk south')
def walk_south():
    walk(0, -1)

@when('walk west')
def walk_west():
    walk(-1, 0)

@when('despair')
def despair():
    print("Waaaaaahhhhhhh!!!")
    print_status()

@when('take THING')
def take(thing):
    print('You take the %s.' % thing)
    inventory.append(thing)
    print_status()

# @when('examine THING')
# def examine(thing):
#     print('You take the %s.' % thing)
#     inventory.append(thing)
#     print_status()

@when('brexit')
def brexit():
    print("Geee, thanks... \nInvoking Article 50 now. Or maybe in a couple of months. Maybe.\nExiting now. *sobs*")
    exit()




start()


