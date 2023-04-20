#filter
#lambda:syntax:lambda args:logic
#x=lambda  x,y,z:x+y-z
from functools import reduce
print(reduce(lambda x,y:x+y,[1,2,3,4,5]))