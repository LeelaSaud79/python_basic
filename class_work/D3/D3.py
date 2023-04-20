# Day3: Sets and dictionaries
student={ 'Ram', 'Priya'}
print(type(student))
student.add('Ram')
student.add('34')
print(student)
set_nums={1,2,3,4,5}
set_nums1={3,4,5,7,9}
a=set_nums & set_nums1# for intersection
print(a)
b=set_nums | set_nums1 #for union
print(b)
# set_nums.is_disjoint(set_nums1)
# print(set_nums)
student.remove('Ram')
print(student)
student.discard('3')
print(student)
x= set_nums.copy()#alwaus use dot
print(x)
set_nums2=({4,5,6,7})
c=set_nums.intersection_update(set_nums2)
print(set_nums)
student.update({7,8,9,0})
print(student)
num=student.pop()
print(student)
#dictionaries
dict_marks={'ram':56,'soya':90,'siya':79}
print(dict_marks)
p=dict_marks['soya']
print(p)
dict_marks['ram']=57
print(dict_marks)
dict_marks['rem']=45
print(dict_marks)
# dict_marks=({'riya':90})
# print(dict_marks)
dict_marks.pop('ram')
print(dict_marks)
a=dict_marks.items()
print(a)
info_people={'ram':{'address':'bagbazar', 'phone':456789}}
print(info_people)
a=info_people['ram']['phone']
print(a)
# dict_marks={'ram':[56,54,89]}
# print(dict_marks)
#conditions
# x=input("enter a number")
# print(type(x))
y=int(input("enter a number: "))
print(y)
print(type(y))
if y%2==0:
    print('even')
else:
    print('odd')









