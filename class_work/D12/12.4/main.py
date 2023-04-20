word='papaya'
newword=word[0]+','.join([char if char!=word[0] else'@' for char in word[1:]])
print(newword)