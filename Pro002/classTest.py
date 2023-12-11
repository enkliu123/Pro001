#类和对象
class washer:
    def __init__(self,weight,height):
        self.weight = weight
        self.height = height

    def describe(self):
        print(f"The weight of the washer is{self.weight}  and height is{self.height}")

haier = washer(70,90)
haier.describe()
xiaomi= washer(60,80)
xiaomi.describe()

