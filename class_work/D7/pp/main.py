# find prime number using range break and continue
# num=int(input('enter a number:'))
# for i in range(5):
#     if num%i==0:
#         print('not a prime number')
#         break
#     else:
#         print('is a prime number')
# print(list(range(2,30)))
user=int(input('enter a number:'))
prime_flag=True
for i in range(2,user):
    if user%i==0:
        prime_flag=False
if prime_flag:
    print('number is prime')
else:
    print('number is not prime')
num=int(input('enter a number:'))
number=0
for x in range(2,num):
    if num%x==0:
        number+=1
if number>=1:
    print('composite')
else:
    print('prime')