class RockMap:

    def __init__(self):
        self.map = [
        [
        "nothing here" for x in range(10)]
            for x in range(10)
        ]
        self.map[4][4] = "booster"
        self.position = (5,5)


    # def move(lat,long):
    #     self.position


a = RockMap()
print(a.map)

