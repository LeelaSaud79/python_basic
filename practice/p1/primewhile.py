# Print a prime number using a while loop:
num=int(input('enter a number: '))
p_flag=True
i=2
while i<=num:
    if num%i==0:
        p_flag=False
        break
    i=i+1
if p_flag==0:
    print('not a prime number')
else:
    print('prime number')
