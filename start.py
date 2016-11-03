#!/usr/bin/env python3


from adventurelib import *

from rockmap import RockMap

map = RockMap()

def walk(x, y):
	map.move_player(x,y)
    print('Walking up %s and right %s...' % (x, y))

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



@when('take THING')
def take(thing):
    print('You take the %s.' % thing)
    inventory.append(thing)

@when('examine THING')
def take(thing):
    print('You take the %s.' % thing)
    inventory.append(thing)


@when('brexit')
def brexit():
    print("Geee, thanks... \nInvoking Article 50 now. Or maybe in a couple of months. Maybe.\nExiting now. *sobs*")
    exit()




start()


