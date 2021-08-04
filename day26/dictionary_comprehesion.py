# new_dict = {new_key:new_value for item in iterable_object}
import random
names = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
score_students = {name:random.randint(1,101) for name in names}
print("All Students = ",score_students)
passed_students = {name:score for name,score in score_students.items() if score >= 60}
print("Passed Students = ",passed_students)

