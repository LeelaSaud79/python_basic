''' Write a function to complete the top 20 most frequent words in the file attached.
 You will need to exclude articles such as "a", "an" and "the"
 Write a function to complete the probability of occurrence of a word in this file.'''
file=open("shakespeare.txt","r")
content= file.read()
# print(content[:1000])
import string
punc=string.punctuation
list_words=[ ]
for char in content.lower():
    if char not in punc:
        if char=="\n":
            list_words.append(" ")
        else:
            list_words.append(char)
content="".join(list_words)
list_word=[]
articles=["","a","an","the","is","i","you","in"]
for word in content.split(" "):
    if word not in articles:
        list_word.append(word)
print(list_word)
print('\n')
print('\n')
#To count each word
d1=dict()
for line in list_word:
    words=line.split(" ")
    for word in words:
        if word in d1:
            d1[word]=d1[word]+1
        else:
            d1[word]=1
print(d1)
#for frquently used 20 words
print('\n')
from collections import Counter
Counter=Counter(d1)
most_occur = Counter.most_common(20)
print(most_occur)
#for probability:
print('Total Number of words in file:',len(list_word))
print('Total no or words in dict:',len(d1))
print('Prob of occurance of word in file:',len(d1)/len(list_word))