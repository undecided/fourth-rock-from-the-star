#!/usr/bin/env python3


from adventurelib import *

from RockMap import RockMap

inventory = []

map = RockMap()
# terrain = RockTerrain()

def print_status():
    print("Status")
    terrain_number = map.get_terrain()
    print("Terrain: %d " % terrain_number) # terrain.get_description(terrain_number)


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

@when('examine THING')
def examine(thing):
    print('You take the %s.' % thing)
    inventory.append(thing)
    print_status()


@when('brexit')
def brexit():
    print("Geee, thanks... \nInvoking Article 50 now. Or maybe in a couple of months. Maybe.\nExiting now. *sobs*")
    exit()




start()


