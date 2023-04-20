class Student:
    name='siya'
    age=25
class faculty(Student):
    best='science'
    exam_grade='A'
class sub(Student):
    fav='Math'
    shift='morning'
siya=faculty()
print(siya.exam_grade)
print(siya.name)
hari=sub()
print(hari.name)
print(hari.shift)

