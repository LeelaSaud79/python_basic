# Program to solve quadratic equation.
import cmath
a=1
b=5
c=6
d=(b**2) - (4*a*c) #first we calculate the discriminant.
first=(-b-cmath.sqrt(d)/2*a)
second=(-b+cmath.sqrt(d)/2*a)
print('The solutions are{0} and {1}'.format(first,second))
