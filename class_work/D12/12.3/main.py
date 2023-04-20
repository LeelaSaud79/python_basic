word='papaya'
newword=word[0]
for char in word[1:]:
    if char!=word[0]:
        newword+=char
    else:
        newword+='@'
print(newword)
#annother method:
newword=word[0]+word[1:].replace(word[0],'@')
#another method:
