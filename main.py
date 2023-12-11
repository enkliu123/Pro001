# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
num1 = 14
num2 = 10.5
Name =  'Helen'
num1 += num2
strName = '........'
# Score = int(input('pls input the scroe:'))
Score = 70
name = 'sixstar'
list = ['one', 'two', 'three']
listInt = [1,2,3,[4,5,6]]
dictStr = { 'name': 'Helen', 'age': 20, 'tel': 123}

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def sort(a, b) :
    return print(a + b)

# different print type
def printType() :
    print("hello,world","welcome to my project",sep='',end='...')
    print('have a nice day!')
    print(type(num1))
    print(type(num2))
    print(type(True))
    print(f'hello,{name}')
    print('my name is %s,年龄是 %d' % (name, num1))
    print(f'my name is {name}, age is {num1}')
    print (f'my input is:{strName}')

# 条件语句
def iftest(Score) :
    if 80< Score <= 100:
        print(f'your score is {Score},so good')
    elif Score <= 60:
        print(f'your score is {Score},so bad')
    else:
        print(f'your score is well')

# 99乘法表
def multi(i, j) :
    i = 1
    while i <= 9:
        j = 1
        while j <= i:
            print(f'{i} * {j}= {j * i}', end="\t")
            j += 1
        print()
        i += 1

# for 循环语句
def fortest() :
    s = 0
    for i in range(1,101) :
        s += i
    print(f'1到100之和计算结果是 = {s}')

#printStrName with Index
#name = 'sixstar'
def printNameWithIndex(name) :
    #index
    print(name[0])   #s
    print(name[-1])  #r
    print(name[-2])  #a
    #split
    print(name[0:4])  #sixs
    print(name[3:])   #star
    print(name[:-1])   #sixsta
    print(name[-5:-1])  #xsta

    print(name[-1::-1])   #从右往左切片选择 ratsxis
    print(name[-1:-5:-1])  # rats 从右往左切片选择，加上步长为1
    # find string
    print(name.find('s',3)) #from 0 to 3, s is at 3
    print(name.find('s',4))  #from 0 to 4, s is not at 4, return null
    # count string number
    print(name.count('s',1))  #from 2 to end count s number=1
    print(name.count('b'))     #count b but not have, return 0
    print(name.replace('s','S')) #SixStar
    print(name.split('x'))  #['si', 'star']

def listTest(list) :
    for i in list :
        print(i)
    list.append('four')
    list.extend('five')
    list.insert(0,'six')
    print(list)
    list.pop(2)
    print(list)
    list.reverse()
    print(list)


#listInt = [1,2,3,[4,5,6]]
#列表嵌套
def listIntTest(list) :
    print(list[3][0])   #4

#dictStr = { 'name': 'Helen', 'age': 20, 'tel': 123}
def dictTest(dict) :
    for i in dict :
        print(i)    #取键值
        print(dict[i]) #取value值
        print()
    print(dict.values()) #dict_values(['Helen', 20, 123])
    print(dict.items())  #dict_items([('name', 'Helen'), ('age', 20), ('tel', 123)]),返回元组格式

#可变参数带*args
def funcTest(*args) :
    print(args)  #以元组形式接收参数
    print(len(args))   #4
    print(type(args))   #tuple

#关键字参数 **kwargs
def funcTest2(**kwargs) :
    print(kwargs)    #{'name': 'enka', 'age': 18}
    print(type(kwargs))  #dict
    print(len(kwargs))   #2

#匿名函数 lambda
funcTest3 = lambda **kwargs : print(kwargs)

#try/exception example /raise exception
def login() :
    pwd = input('please input your password: ')
    if len(pwd) >=6 :
        return 'your password is valid'
    raise Exception ('invalid password')

#递归函数,计算3以内的数的和
def sum_num(num):
    if num == 1:
        return 1
    return num+sum_num(num-1)

#闭包的应用,外部函数嵌套内部函数，
def outer(step):
    num =1
    def inter() :
        nonlocal  num #生命变量为父级变量，使能被修改
        num += step
        print(num)
    return inter  #返回函数名，没有括号，返回值被保存

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
#     ot = outer(3)
#     for i in range(5) :
#         ot()       #执行5次，值分别是4 7 10 13 16
     # print(sum_num(4))
     print_hi(Name)
     # printType()
     # sort(num1, num2)
     # iftest(Score)
     # multi (9, 9)
     # fortest()
     # printNameWithIndex(name)
     # listTest(list)
     # listIntTest(listInt)
     # dictTest(dictStr)
     # funcTest(1,2,3,'abc')
     # funcTest2(name='enka', age =18)
     # funcTest3 (name='helen', age=18)
     #    login()
    # try:
    #     print(login())
    # except Exception as e:
    #     print(e)

