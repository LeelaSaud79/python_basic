# Day 4:
import random
comp_input=random.choice([0,1,2])
user_input= int(input('Enter 0 for rock, 1 for paper , 2 for scissor :'))
'''choices={0:'rock',
         1:'paper',
         2:'scissor'}
print('you chose',choices[user_input])
print('computer chose',choices[comp_input])'''
print(comp_input)
if user_input==comp_input:
    print('draw')
elif user_input==0 and comp_input==1:
    print('computer win')
elif user_input ==0 and comp_input==2:
    print('user win')
elif user_input==1 and comp_input==0:
    print('user win')
elif user_input==1 and comp_input==2:
    print('computer win')
elif user_input==2 and comp_input==0:
    print('user win')
elif user_input==2 and comp_input==1:
    print('computer win')
