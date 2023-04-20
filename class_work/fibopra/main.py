# fibonaccii number
num=int(input('enter a number of sequence:'))
if num==1:
    print('0')
elif num==2:
    print('0, 1')
else:
    prev_num=0
    curr_num=1
    print('0,1',end=',')
    for i in range(num-2):
        new_num = prev_num+curr_num
        print(new_num, end=',')
    prev_num=curr_num
    curr_num=new_num