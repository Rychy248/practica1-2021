#Hello World!
result = [] 

with open("file1.txt","r") as file1:
    list_1 = file1.readlines()

with open("file2.txt","r") as file2:
    result = [int(num) for num in file2.readlines() if num in list_1]

print(result)


