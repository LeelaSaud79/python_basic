# 5.WAP to print all the prime numbers upto a given number.
num=int(input('Enter a number:'))
for num in range(0,num+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
            else:
                print(num,end=',')