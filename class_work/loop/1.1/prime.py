# WAP to ask the user for a number and determine whether the number is prime or not.
#using for loop:
num=int(input('enter a number:'))
f_flag=True
for i in range(2,num):
    if num%i==0:
        f_flag=False
        break
if f_flag==0:
    print('not a prime number')
else:
    print('prime number')
#Using while loop:
user=int(input("Enter a number:"))
p=2
q_flag=True
while p<=user:
    if user%p==0:
        q_flag=False
        break
    p+=1
if q_flag==0:
    print('not a prime number')
else:
    print(' prime number')


