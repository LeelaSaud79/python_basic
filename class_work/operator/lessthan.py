class point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    def __lt__(self, other):
        self_call=(self.x**2)+(self.y**2)
        other_call=(other.x**2)+(other.y**2)
        return (self_call<other_call)
p1=point(1,2)
p2=point(5,6)
p3=point(0,9)
print(p1<p2)
print(p3<p1)
print(p2<p3)