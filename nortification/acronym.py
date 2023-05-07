# Here we are asking for the phrase
user_input = str(input("Enter a phrase :"))
word = user_input.split()
Acronyms = " "
for j in word:
     Acronyms = Acronyms +str(j[0].upper())

print(Acronyms)