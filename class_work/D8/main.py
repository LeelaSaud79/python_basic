#dict using comprehansion
list1=[7,8,15,22]
dict={num:'even' if num%2==0 else'odd' for num in list1}# ternary operator in python
print(dict)