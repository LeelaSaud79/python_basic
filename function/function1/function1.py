#1.Write a Python function to find the Max of three numbers.
def max(a,b,c):
    if a>b and a>c:
        print('a is maximum number.')
    elif b>a and b>c:
        print('b is maximum.')
    else:
        print('c is maximum.')
    return
max(3,5,9)