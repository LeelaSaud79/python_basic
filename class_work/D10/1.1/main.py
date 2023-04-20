# def add(*args):
#     sum=0
#     for num in args:
#         sum+=sum
#         return sum
# add(2,3)
# def sub(**kwargs):
import math
# list(map)
list1=[(2,3),(4,5),(5,6),(0,3),(5,3)]
list2=[(1,2),(3,4),(4,5),(0,1),(1,9)]
def distance(p1,p2):
    return math.sqrt(math.pow(p1[0] - p2[0], 2) + math.pow(p1[1] - p2[1], 2))
dist=list(map(distance,list1,list2))
print(dist)


