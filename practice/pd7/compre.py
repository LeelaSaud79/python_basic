# practice of day7 i.e comprehansion:
list=['23','lee','oreo']
print({name.upper() for name in list})# brackets define the collectin.
list_num=[2,5,8]
list_num_sq=tuple(num**2 for num in list_num)#we have to declare for tuple since it also uses parenthess.
print(list_num_sq)
list=[1]
for item in list:
    print(item)
    list.append(item+1)