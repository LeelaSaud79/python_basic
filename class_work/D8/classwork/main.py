# classwork
dict_marks={'ram':[78,34,56,77,90],
'sita':[34,56,56,7,9],
'hari':[23,45,67,89,67],
'gopi':[23,34,56,7,8]
}
dict_avg={name:sum(marks)/len(marks) for name,marks in dict_marks.items()}
print(dict_avg)
dict_pass={name:'pass'if avz>=40 else'fail' for name,avz in dict_avg.items()}
print(dict_pass)


