# Object orientd programming:
# A class is a representation of real world objects.class is a data type.
class student:
    name='Jungkook'#starting
    age=23
x=student()
print(type(x))
y=student()#x is instance /object of student class
print(x.name)
x.name='ram'
print(x.name)
print(y.name)
z=student()
print(z.name)