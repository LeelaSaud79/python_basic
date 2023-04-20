a=2
b=5
print(a//b)
print(a**b)
a&=a
print(a)
if a<3 and b>2:
    print('true')
c=2
print(a is c)
# print(a===c)
st_name=['1','2','3']
print('1' not in st_name)
#another program
list=['lee','pro','yes',34]
print(list[-3])
print(list[1:3])
if 'lee' in list:
    print('yes')
list[2]='weee'
print(list)
list.insert(1,'356')
print(list)
list.append('pree')
print(list)
list_1=[1,3,4,'uma']
list.extend(list_1)
print(list)
list.remove('pro')
print(list)
list.pop(1)
print(list)
# del list
# print(list)
# list.clear()
# print(list)
list=list.copy()
print(list)
fruits=['apple','3','3','34','mango']
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
#set
set={'12',90,'hee','was'}
set.update(fruits)
print(set)
# set.remove(120) cause error cause 120 is not in the list but discard doesn't create error
# print(set)
set.discard('hee')
print(set)
x=set.pop()
print(x)
print(set)
# set.clear()
# print(set)
# del set
# print(set)
