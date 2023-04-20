# Implement the best of 3 version of ROCK, PAPER AND SCISSORS
import random
count_user, count_comp, count_draw = 0, 0, 02
for i in range(3):
    comp_input = random.choice([0, 1, 2])
    win_com = [(1, 0), (0, 2), (2, 1)]
    user_input=int(input('0 for rock, 1 for paper and 2 for scissors:'))
    while user_input not in [0,1,2]:
        user_input=int(input('0 for rock, 1 for paper and 2 for scissors:'))
    choices={0:'rock',
             1:'paper',
             2:'scissors'}
    if(user_input,comp_input) in win_com:
         print('user win')
         count_user+=1
    elif user_input==comp_input:
         print('draw')
         count_draw+=1
    else:
        print('computer win')
        count_comp+=1
print('total no of user win:',count_user)
print('total no of comp win:',count_comp)
print('total no of draw:',count_draw)