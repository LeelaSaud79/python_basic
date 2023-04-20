# game program: rock, paper & scissor:
# 0 for rock, 1 for paper and 2 for scissors:
#method1:
import random
user_input=int(input('Enter 0 for rock, 1 for paper, 2 for scissors: '))
comp_input=random.choice([0,1,2])
print(comp_input)
if user_input==comp_input:
    print('withdraw')
elif user_input==0 and comp_input==1:
    print('computer win')
elif user_input==0 and comp_input==2:
    print('user win')
elif user_input==1 and comp_input==0:
    print('user win')
elif user_input==1 and comp_input==2:
    print('computer win')
elif user_input==2 and comp_input==0:
    print('user win')
elif user_input==2 and comp_input==1:
    print('computer win')

