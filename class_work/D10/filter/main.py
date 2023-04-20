'''comprenhension=logic loop condition
filter is same as comprenhension.
filter syntax:filter(function,colln)i.e takes only one collection
function should always return the boolean value'''
list1=[1,2,3,4,4,-7,9.9]
x=list(filter(lambda x: x>2,list1))
print(x)
# wap using the filter points=[(0,0),(5,2),(3,4)] to filter out points with distance >=5.
import math
# points=[(1,1),(2,5),(8,9)]
# points2=list(filter(lambda p:math.sqrt(p[0]**2+p[1]**2)<5,points))#p is tuple
# print(points2)
'''marks={'ram'=[56,78,99,45],'sita':[23,45,67],'gita'=[23,45,67]
using map find the average
use filter to get students avg marks graeter than 60'''
marks={'ram':[56,78,99],'sita':[23,45,67],'giya':[23,45,67]}
avg=list(map(lambda x:sum(x[1])/len(x[1]), marks.items()))lambda return only the number here.
avg=dict(map(lambda x:(x[0],sum(x[1])/len(x[1])),marks.items()))
print(avg)
greater=dict(filter(lambda x:x[1]>60,avg.items()))
print(greater)

