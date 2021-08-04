"""List comprehesion"""

def space():
    print("-_"*20)

numbers = [1,2,3]

space()
new_list = [item+1 for item in numbers]
print(new_list)
second_list = [n-2 for n in new_list]
print(second_list)
space()
name = "Ricardo"
print(name)
list_name = [character for character in name]
print(list_name)
space()
num_list = [num*2 for num in range(1,5)]
print(num_list)
space()
names = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
print(names)
#[new_item for item in list if test]
shorth_names = [name for name in names if len(name)<=4]
print(shorth_names)
uper_names = [name.upper() for name in names if len(name)>4]
print(uper_names)
space()
space()
#EXCERCISE ONE
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55] 
squared_numbers =  [num**2 for num in numbers]
print(squared_numbers)

#EXCERCISE TWO
result = [num for num in numbers if num%2==0]
print(result)




