'''Assignment:
1. WAP to check whether the number is palindrome or not.
Source code:'''
x_word=(input('Enter a word:'))#only for string
print(x_word)
print(type(x_word))
if x_word==x_word[-1::-1]:
    print('palindrome')
else:
    print('not palindrome')

# 2. WAP to find if a number is multiple of 5 or not.
y=int(input('Enter a number: '))
print(y)
print(type(y))
if y%5==0:
    print('y is multiple of 5')
else:
    print('y is not multiple of 5')

#3 WAP to find if a word is vowel or not.
# w_input=input('Enter a string :')
# print(w_input)
# print(type(w_input))
'''w_input=input('Enter a word').lower())
if 'a' in w_input or 'e' in w_input or  'o' in w_input or 'o' in w_input or 'u' in w_input:
    print('vowel is in string')
else:
    print('vowel is not in string')'''
user_input= set(input('Enter a string: ').lower()) # another method
set_of_vowel={'a','e','i','o','u'}
if user_input and set_of_vowel:
    print('there is a vowel')
else:
    print('there is not a vowel')

