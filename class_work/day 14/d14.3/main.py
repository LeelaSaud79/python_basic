# construct child as a constructor.Priority is given on the basis of DFS in multiple inheritance.
class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Guard(Employee):
    def __init__(self,shift,name,age):
        self.shift=shift
        Employee.__init__(self,name,age)
hari=Guard(name='hari',age=24,shift='morning')
print(hari.name,hari.age,hari.shift)
print(hari.__dict__)#key value association
print(Guard.__mro__)#method resolution order