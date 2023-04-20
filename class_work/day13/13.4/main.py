#inheritance:
class Employee:
    name='ram'
    age=30
class SoftwareEngineer(Employee):
    qualification='B tech'
    experience=8
class CleaningsStaff(Employee):
    shift='morning'
ram=SoftwareEngineer()
print(ram.qualification)
print(ram.name)
hari=CleaningsStaff()
print(hari.name)
print(hari.shift)