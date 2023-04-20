#method 4 for rock paper and scissors:
import random
user_input=int(input('0 for rock, 1 for paper and 2 for scissors: '))
comp_input=random.choice(([0,1,2]))
print(comp_input)
if user_input==comp_input:
    print('withdraw')
elif (user_input==1 and comp_input==0 or
      user_input==2 and comp_input==0 or
      user_input==2 and comp_input==1):
    print('user win')
else:
    print('computer win')