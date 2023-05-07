
x = 50
def fool():
     global x
     x = 90
fool()
print(x)

# Checking the palindrome
string = "Welcome"
if string == string[::-1]:
    print("string is palindrome.")
else:
    print("string is not palindrome")

# Removing the white space and duplicate alphabet
word = "Friends are not as good as you think."
new_word = "".join(word.split())
words = "".join(set(string))
print(new_word)
print(words)


# Generating a random integer
import random
random_integer = random.randint(10,100)
print(random_integer)

# Counting the number of words in string

xyz = " Hello everyone"
new = len(xyz)
print(new)
