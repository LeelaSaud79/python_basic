# Write a Python function to calculate the factorial of a number
# (a non-negative integer). The function accepts the number as an argument.
num=int(input('Enter a number:'))
def factorial(z):
    if z==1:
        return 1
    else:
        return (z*(factorial(z-1)))
result=factorial(num)
print(result)