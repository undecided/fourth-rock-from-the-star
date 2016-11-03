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

        self.position[0] += x
        self.position[1] += y
        print(self.map[self.position[0]][self.position[1]].description)

    def get_terrain(self):
        pos = self.position
        square = self.map[pos[0]][pos[1]]
        return square.terrain


class Square():
    def __init__(self, description):
        self.description = description
        self.terrain = random.randint(0, 15)


a = RockMap()
print(a.position, a.get_terrain())
a.move_player(-1,-1)
print(a.position, a.get_terrain())

