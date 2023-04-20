#incapsulation: It is the process of hiding information.
# Any particular that have two underscore is private.for protected one underscore.
class Employee:
    def __init__(self,name,age):       #we can directly assign salary.
        self.__salary=100000
        self.name=name
        self.age=age
    def dispatch_salary(self):
        print(self.__salary,'dispatched')
ram=Employee('ram',25)
print(ram.name)
print(ram.__dict__)
ram.dispatch_salary()