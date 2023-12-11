#继承父类并重写方法
class Parent:
    def __init__(self):
        self.type = 'old'
        self.year = 80

    def displayName(self):
        print(f'type is {self.type} and year is {self.year}')

class Son(Parent):
    def __init__(self):
        self.type = 'new'
        self.year = 20

    def displayName(self):
        print(f'type is {self.type} and year is {self.year}')
        super().__init__()
        super().displayName()

        Parent().__init__()
        Parent().displayName()

class Child(Parent):
    pass

son = Son()
son.displayName()

child = Child()
child.displayName()