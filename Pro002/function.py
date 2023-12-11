#装饰器和闭包
import time
def timeit(func):
    def inner():
        start = time.time()
        func()
        end = time.time()
        print(f'login timer is {end-start}')
    return inner


@timeit
def login():
    user = input("Enter your username: ")
    password = input("Enter your password: ")
    choice = int(input(f"user is {user} and password is {password}, pls confirm your password and press 1:"))
    if choice == 1:
        print("Login Successful")

login()