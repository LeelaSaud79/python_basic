# Day2:List, tuple, slicing
num=['Ram','Priya','Mango','54']
print(num)
print(num[2])#first item has index 0
print(num[2:4])#2 is included and 4 is not included
print(num[-2:-1:1])#negative index starts from end
print(num[:2])
print(num[2:])
num.append('Thor')
print(num)
# num.append('2','riya') this is invalid
num.extend(['23','Riya', 'priya'])
print(num)
num.insert(3,'Please')
print(num)
num.remove('Please')
print(num)
num.pop(2)
print(num)
del num[0]
print(num)
# num.clear(): To empty the list
num.sort()
print(num)
num.sort(reverse= True)#T is in uppercase
print(num)
num.reverse()
print(num)
num=num.copy()# Use to copy
print(num)
# slicing(start, end, step)
x=slice(2,4)
print(num[x])
#tuples
tuple=('Elena','Jk','89','wee','89')
print(tuple)
print(tuple[4])
print(tuple[-4:-2])
