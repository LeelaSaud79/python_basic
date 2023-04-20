# Write a function called digit_sum that can take any number of
# integer arguments takes returns the sum of all that number's digits.Here we first convert number
# to string and then after result again convert into int.
# n=int(input('Enter a number:'))
n=int(input('Enter  positive number:'))
def digit_sum(num):
    sum=0
    while(num>0):
        sum=sum+(num%10)
        num=num//10
    return sum
print(digit_sum(n))