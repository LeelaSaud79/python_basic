'''Higher order functions: It can take args as other functions. It has three important factors
1.map no of arguments is equal to number o collection map algortimh should cast in list or tuple.only.'''
list1=[1,2,3]
list2=[2,4,4]
def add(a,b):
    return a+b
x=list(map(add,list1,list2))
print(x)
marks_english=[56,78,90]
marks_nepali=[78,67,89]
marks_computer=[23,45,67]
def avz(a,b,c):
    return (a+b+c)/3
z=list(map(avz,marks_computer,marks_nepali,marks_english))
print(z)

