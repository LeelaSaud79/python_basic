#practice of day 10 i.e filter and lambda
'''list1=[3,4,5,6]
x=list(filter(lambda x:x<5,list1))
print(x)'''
import math

'''import math
points=[(1,4),(5,6),(7,8)]
points1=list(filter(lambda p:math.sqrt(p[0]**2+p[1]**2)<5,points))#to print the distance less than 5
print(points1)'''
'''marks={'ram':[23,45,67,89],'siya':[34,56,78,90],'ele':[45,56,7,8,]}
avg=dict(map(lambda x:(x[0],sum(x[1])/len(x[1])),marks.items()))
print(avg)
greater=dict(filter(lambda x:(x[1]>60),avg.items()))
print(greater)'''
'''import math
x_coordinates=[1,2,3]
y_coordinates=[4,5,6]
z_coordinates=[3,4,5]
distance=list(map(lambda x,y,z:math.sqrt(x**2+y**2+z**2),x_coordinates,y_coordinates,z_coordinates))
print(distance)'''
# WAP to print the distance of two list
'''import math
list1=[(2,3),(4,5),(7,8)]
list2=[(2,3),(3,4),(5,6)]
def distance(p1,p2):
    return math.sqrt(math.pow(p1[0]-p2[0],2)+math.pow(p1[1]-p2[1], 2))
dist=list(map(distance,list1,list2))
print(dist)'''
def f():
    return x+2
print(type(f))
print(type(lambda x:x+1))
g=lambda x:x+5
print(g(6))
