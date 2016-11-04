#!/usr/bin/env python3

import random

from adventurelib import *

from RockMap import RockMap
import Jimmy
import Terrain

jimmy_loc = Jimmy.jimmy_generate(9,9)

inventory = []

map = RockMap()

def win(pos):
    if Jimmy.jimmy_distance((pos[0], pos[1]), jimmy_loc) <= 1:
        print("You found Jimmy!! You win!!")
        exit()

def print_status():
    print("\nCurrent status:")
    pos = map.position
    jimmy_distance = Jimmy.jimmy_distance((pos[0], pos[1]), jimmy_loc)
    print("You are %d away from Jimmy" % jimmy_distance)
    win(pos)
    if len(inventory) > 0:
        print("You have %d items in your backpack. Don't ask me what." % len(inventory))
    print("Jimmy says: %s" % Jimmy.jimmy_comment(jimmy_distance))
    print("You look down and see %s" % Terrain.get_description(map.get_terrain()))

def walk(x, y):
    print_status()
    map.move_player(x,y)
    print("\nYou're on the move!")
    print("You feel %s beneath your feet" % Terrain.get_description(map.get_terrain()))
    if not Terrain.is_passable(map.get_terrain()):
        print("You decide that maybe walking through %s isn't such a hot idea" % Terrain.get_description(map.get_terrain()))
        print("!!! You've run back to your previous position !!!")
        map.move_player(x*-1, y*-1)
    print()

@when('walk north')
def walk_north():
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
    print('You take %s.' % thing)
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


print_status()

start()


