# inheritance:
# pass is a filler
class A:
    pass
    # def print_name(self):
    #     print('class A')
class B(A):
    pass
class C:
    def print_name(self):
        print('class C')
class D(B,C):
    pass
x=D()
x.print_name()
