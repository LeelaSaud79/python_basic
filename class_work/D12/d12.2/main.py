freq_dict={}
word='Papaya'
for char in word.lower():
    if char not in freq_dict.keys():
        freq_dict[char]=1
    else:
        freq_dict[char]+=1
print(freq_dict)