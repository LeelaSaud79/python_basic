#function:takes n input and m outputs.
def simple_interest(principle, time, rate):
    '''This is a test function which takes
     three input'''
    interest=(principle*time*rate)/100
    return interest
dict1={'principle':14000,'rate':12,'time':3}
i=simple_interest(**dict1)#keyword way
print(i)
interest=simple_interest(10000,3,2)
print(interest)

