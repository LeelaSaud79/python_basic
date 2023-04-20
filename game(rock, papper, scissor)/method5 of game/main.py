# mathod 5 for rock paper and scissor:
import random
user_input=int(input('0 for rock, 1 for paper, 2 for scissors: '))
comp_input=random.choice([0,1,2])
print(comp_input)
if user_input==comp_input:
    print('withdraw')
elif (user_input-comp_input)%3:
    print('user win')
else:
    print('computer win')
