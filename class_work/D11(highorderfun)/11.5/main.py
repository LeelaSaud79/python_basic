#example of json
import json
#open('test.json','r') as file: we don't have to use file close()
f=open("test.json","r")
dict_prices=json.load(f)
print(dict_prices)
f.close()