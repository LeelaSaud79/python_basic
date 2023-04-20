#what happens when there is constructor in inheritance?
class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Guard(Employee):
    shift='morning'
hari=Guard('hari',27)
print(hari.name)