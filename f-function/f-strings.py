# Align strings with f-string
str = "Padma"
age = 20
print(f"|{age <= 19} |{age :^5}|")

# F-strings for dictionary variable
person = {"Name": "leela", "Marks": 90}
print(f"My name is{person['Name']} and my marks is {person['Marks']} in maths.")

# F-strings for binary and hexadecimal
x = 600
print(f"x={x:b}")
print(f"x={x:x}")

# f-strings for date and time
import datetime
now = datetime.datetime.now()
print(f"Today is {now: %B %d, %Y}")

fee = 40000
print(f"salary is {fee:}.")


# for scientific notations
x = 12356743210.567843234
print(f"x:{x:e}")