#function programs:
def name(name):
    '''This is a simple program used to print a name statement'''
    print('hello'+ name)
name('ram')
def myfunc():
    '''variable defines inside a function is not visible from outside the function.
    so they are called local scope.'''
    x=10
    print(x)
x=20
myfunc()
print(x)