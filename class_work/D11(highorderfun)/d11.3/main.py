import pickle
info=pickle.load(open("test.pkl","rb"))
print(info)#wap using map to find out
import math
x_coordinates=[1,2,3,4]
y_coordinates=[3,4,5,6]
z_coordinates=[2,3,4,8]
dish = list(map(lambda x,y,z:math.sqrt(z**2+y**2+z**2),x_coordinates,y_coordinates,z_coordinates)
print(dish)