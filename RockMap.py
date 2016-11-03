import random

class RockMap:

    def __init__(self):
        self.map = [
        [
         Square("nothing here") for x in range(10)]
            for x in range(10)
        ]
        self.map[4][4] = Square("booster")
        self.position = [5,5]

    def move_player(self, x, y):
        newx = self.position[0] + x
        if(newx > 9):
            newx = 0
        elif(newx < 0):
            newx = 9
        newy = self.position[1] + y
        if(newy > 9):
            newy = 0
        elif(newy < 0):
            newy = 9
        self.position[0] = newx
        self.position[1] = newy
        print(self.map[self.position[0]][self.position[1]].description)

    def get_terrain(self):
        pos = self.position
        square = self.map[pos[0]][pos[1]]
        return square.terrain


class Square():
    def __init__(self, description):
        self.description = description
        if random.randint(0,4) == 3:
            self.terrain = random.randint(0, 15)
        else:
            self.terrain = 0


a = RockMap()
print(a.position, a.get_terrain())
a.move_player(-1,-1)
print(a.position, a.get_terrain())

