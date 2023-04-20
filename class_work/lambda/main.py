'''Map->map(fun,collection)
lambda->lamda args:logic
lambda can be used only for simple mathematical expression.
We can use the lamda in other function also by properly defining.'''
# x=list(map(lambda x,y:x+y,[1,2,3],[3,4,5]))
# print(x)
def f(x):
   return x+1
print(type(f))
print(type(lambda x:x+1))
g= lambda x:x+1
print(g(6))
