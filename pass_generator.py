import os
import random
c= lambda: os.system("clear")

def clean():
    input("\n\nPress enter, to continue....")
    c()


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
        's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
        'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

hight = nr_letters + nr_symbols + nr_numbers
pypassword = ""
for i in range(hight):
    rand_sign = random.randint(0,2)
    if rand_sign == 0:
        if nr_letters==0:
            rand_sign = random.randint(1,2)
            if rand_sign == 1:
                if nr_symbols == 0:
                    pypassword += random.choice(numbers)
                    nr_numbers -=1
                else:
                    pypassword += random.choice(symbols)
                    nr_symbols -=1
            else:
                if nr_numbers == 0:
                    pypassword += random.choice(symbols)
                    nr_symbols -=1                   
                else:
                    pypassword += randomj.choice(numbers)
                    nr_numbers -=1
        else:
            pypassword += random.choice(letters)
            nr_letters -=1
    elif rand_sign == 1:
        if nr_symbols==0:
            rand_sign = random.choice([0,2])
            if rand_sign == 0:
                if nr_letters == 0:
                    pypassword += random.choice(numbers)
                    nr_numbers-=1
                else:
                    pypassword += random.choice(letters)
                    nr_letters-=1
            else:
                if nr_numbers ==0:
                    pypassword += random.choice(letters)
                    nr_letters-=1
                else:
                    pypassword += random.choice(numbers)
                    nr_numbers-=1
        else:
            pypassword += random.choice(symbols)
            nr_symbols-=1

    elif rand_sign == 2:
        if nr_numbers==0:
            rand_sign = random.randint(0,1)
            if rand_sign == 0:
                if nr_letters == 0:
                    pypassword += random.choice(symbols)
                    nr_symbols -=1
                else:
                    pypassword += random.choice(letters)
                    nr_letters-=1
            else:
                if nr_symbols == 0:
                    pypassword += random.choice(letters)
                    nr_letters-=1                   
                else:
                    pypassword += random.choice(symbols)
                    nr_symbols-=1
        else:
            pypassword += random.choice(numbers)
            nr_numbers -= 1
print(f"Your new password is {pypassword}")
clean()
