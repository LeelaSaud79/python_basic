import pickle
file="mydata.pkl"
fileobj=open(file,'rb')
mydata=pickle.load(fileobj)
print(mydata)
print((type(mydata)))