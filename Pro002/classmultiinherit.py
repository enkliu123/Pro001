#多继承 父亲类 母亲类
class Dad(object):
    def test(self):
        print("Dad")

class Mon(object):
    def demo(self):
        print("Mon")

class Son(Dad,Mon):
    pass

son = Son()
son.test()
son.demo()
