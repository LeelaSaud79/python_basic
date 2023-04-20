#decorator:it is way of using higher order function created by user.Decorator are wrappers.It modify the function functionality.
from datetime import datetime
def logger(func):
    def inner_func():
        with open('log.txt','a')as file:
            file.write(func.__name__+" executed "+str(datetime.now())+'\n')
        # print(func,'executed')#wrapper logic
        # if permission:
        func()
    return inner_func#return only refernce
@logger#decorator
def add():
    print('this is a function')
@logger#decorator
def sub():
    print('this')
add()
sub()



