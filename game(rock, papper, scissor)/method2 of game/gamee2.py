#method 2 for rock paper and scissors:
import random
user_input=int(input('0 for rock, 1 for paper, 2 for scissors:'))
comp_input=random.choice([0,1,2])
choices={0:'rock',
        1:'paper',
        2:'scissors'}
print('you chose',choices[user_input])
print('computer chose',choices[comp_input])
if user_input==comp_input:
        print('wihdraw')
elif user_input==0 and comp_input==1:
        print('computer win')
elif user_input==0 and comp_input==2:
        print('user win')
elif user_input==1 and comp_input==0:
        print('user win')
elif user_input==1 and comp_input==2:
        print('computer win')
elif user_input==2 and comp_input==0:
        print('computer win')
elif user_input==2 and comp_input==1:
        primt('user win')
