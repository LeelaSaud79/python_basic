''' WAP to get a string from a given string where all the occurance of
its first char have been changed to
 '@'except the first char itself.'''
string='schools'
newword=string[0]+string[1:].replace(string[0],'@')
print(newword)