# Write a Python function that accepts a string and
# calculate the number of upper case letters and lower case letters.
def char_count(user_input):
    uppercase_count=0
    lowercase_count=0
    for char in user_input:
        if char.isupper():
            uppercase_count+=1
        else:
            lowercase_count+=1
    return uppercase_count,lowercase_count
a,b=char_count('The quick Brow Fox')
print('Number of uppercase characters:',a)
print('Number of lowercase characters:',b)