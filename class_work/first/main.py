#program to find the total marks, percentage and number of passed students using using comprenhension method.
student_marks={'Ram':[90,23,57,89,12,34],
               'Siya':[78,23,11,90,67,56],
               'Uma':[56,78,98,34,45,66]}
student_avg={name:sum(marks)/len(marks) for name,marks in student_marks.items()}
print(student_avg)
student_per={name:'pass' if avg>=50 else 'fail' for name,avg in student_avg.items()}
print(student_per)
student_pass={name :for name,result in student_per.items() if result=='pass'}
print(student_pass)
