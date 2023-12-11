#魔法方法
class Roast:
    def __init__(self):
        self.time = 0
        self.status = 'not good'
        self.season = []

    def roast(self, time):
        self.time += time
        if 0<time<=3:
            self.status = 'not good'
        elif 3<time<=8:
            self.status = 'good'

    def seasoning(self, season):
        self.season.append(season)

    def __str__(self): #显示信息
        return f'Roast time: {self.time}, status: {self.status}, season: {self.season}'


hs = Roast()
hs.roast(2)
hs.seasoning('salut')
print(hs)
hs.roast(3)
hs.seasoning('sugar')
print(hs)