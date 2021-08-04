import pandas

student_dict = {
    "Students" : ["Angela","James","Lily"],
    "Score" : [56,76,98]
}
#Looping througth dictionaries:
"""
for key,value in student_dict.items()
    print(key," ",value)
"""
students_data_frame = pandas.DataFrame(student_dict)
print(students_data_frame)
#Looping througth Data Frame:
"""
for key,value in students_data_frame.items():
   print(key," ",value)
"""
#Looping througth rows of a Data Frame:
for (index, row) in students_data_frame.iterrows():
    if row.Students == "Angela":
        print(f"{row.Students} "*3,end=" ")
    else:
        print(row.Students,end=" ") #row is a pandas series
    print(row.Score)
    #print(index)

