#PEP recomend don't use the except, alone, becase
"""
for example
try:
    with open("a_file.txt") as file: #thing the file exist
        file.read()
    
    my_dict = {"key1":"Hello","key2":"World","key3":"Other"}
    print(my_dict["key4"]) #the error here, is 'keyError'
except:
    #Creating a file
    with open("a_file.txt","w") as file:
        file.write("File created\n")

    THe file here dosen't the problem, the problem was the dictionary
    that's why you haven't use a except alone
"""


try:
    file = open("a_file.txt")
    file.read()
    my_dict = {"key1":"Hello","key2":"World","key3":"Other"}
    #print(my_dict["key4"]) #the error here, is 'keyError'
except FileNotFoundError:
    #if it haven't finded, creat it
    file = open("a_file.txt", "w")
    file.write("File created\n")
except KeyError as error_messegue:
    print(f"That {error_messegue} key dosen't exist")
else:
    """This block of code, will be executed if dosen't happen any error"""
    with open("a_file.txt") as file:
        print(file.read())
finally:
    """File is executed if happen an error or not"""
    file.close()
    print("File closed")


#Raise, let us to trigger our own error
try:
    print("Hi i will make an error"+no_exist_variable)
except NameError as VarName:
    print(f"Error on the variable {VarName}")
else:
    no_exist_variable = "Now it exist"
    print("Else")
finally:
    """Playing with raise errors"""
    #raise error_name("Messegue_to_error")
    #raise TypeError("Hi a made it :) jejeje")

#practice example
height = float(input("Height: "))
weight = int(input("weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 metters")

bmi = weight / height ** 2
print(bmi)
