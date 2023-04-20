# WAP to count the total number of characters(character frequency) in string.
#number of characters:
string=input('Enter a character:')
count=0
for i in string:
    count+=1
print(count)
#frequency of character:
fre_dict={}
word='Schools'
for char in word.lower():
    if char not in fre_dict.keys():
        fre_dict[char]=1
    else:
        fre_dict[char]+=1
print(fre_dict)