#多态性，一种调用方式实现不同执行结果

class Dog(object):
    def wordDog(self):
        print("I am dog")

class blackDog(Dog):
    def wordDog(self):
        print("I am blackdog")

class whiteDoy(Dog):
    def wordDog(self):
        print("I am whitedog")

def workDog(Dog):
    Dog.wordDog()

D1 = blackDog()
D1.wordDog()
D2 = whiteDoy()
D2.wordDog()


#类方法的使用
class Person(object):
    age = 50
    @classmethod
    def getage(cls):
        print(cls.age)

    @classmethod
    def setage(cls,age):
        cls.age = age

p =Person()
p.setage(40)
p.getage()

