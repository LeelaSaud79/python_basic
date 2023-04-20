# print a prime number using a while loop
p_flag=True
num=int(input('enter a number:'))
i=2
while i<=num:
    if num%i==0:
        p_flag=False
        break
    i=i+1
if p_flag==0:
    print('num is not prime')
else:
    print('not a prime')