# use of range
print(list(range(2,19)))
# for item in range(1,18):
#     print(item)
# WAP to take and input from the user and check if its prime.
num= int(input('Enter a number:'))
prime_flag=True
for i in range(2, num):
    if num % i==0:
        prime_flag=False
if prime_flag:
    print ('number is prime')
else:
    print('number is not prime')

