#method 3 for rock, paper and scissors:
import random
user_input=int(input('0 for rock, 1 for paper, 2 for scissors: '))
comp_input=random.choice([0,1,2])
win_comb=[(0,2),(1,0)],(2,1)
if user_input==comp_input:
    print('withdraw')
elif (user_input,comp_input) in win_comb:
    print('userwin')
else:
    print('computerwin')