def char_count(user_input):
    uppercase_count=0
    lowercase_count=0
    for char in user_input:
        if char.isupper():
            uppercase_count+=1
        elif char.islower():
            lowercase_count+=1
    return uppercase_count,lowercase_count
a,b=char_count("Priya")
print(a,b)
