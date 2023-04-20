# WAP that asks the user how many fibonacci number to generate and then generates them.
num=int(input('Enter a number of sequence:'))
if num==1:
    print('0')
elif num==2:
    print('01')
else:
    prev_num=0
    curr_num=1
    print('0,1',end=',')
    for i in range(2,num):
        new_num =prev_num+curr_num
        print(new_num, end=',')
        prev_num=curr_num
        curr_num=new_num
