#CREATED BY RYCHY, contact me -> jorgeajrhh@gmail.com

import os
import random
c= lambda: os.system("clear")

def clean():
    input("\n\nPress enter, to continue....")
    c()

#DAY PROJECT
#Password Generator Project
# con el random.schuffle() se hubiera podido simplificar un monton esto
# el shuffle revuelve todo, lo que nos da la aletoriedad que con la funcion
# nos matamos, aunque tambien la lista ya ordenada se podia desordenar.

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


#Excercise four stop = int(input("Give me a stop number, where do you want stop; ")) stop_var = stop+1

fizz_numbers = []
buzz_numbers = []
fizz_buzz_numbers = []
no_fizz_buzz_numbers = []

for number in range(2,stop_var,1):
    if number%3==0 and number%5==0:
        print("FizzBuzz")
        fizz_buzz_numbers.append(number)
    elif number%3==0:
        print("Fizz")
        fizz_numbers.append(number)
    elif number%5==0:
        print("Buzz")
        buzz_numbers.append(number)
    else:
        print(number)
        no_fizz_buzz_numbers.append(number)

print(f"\nThe numbers, fizz, buzz or fizzBuzz finded are:")
print(f"Fizz = {fizz_numbers}")
print(f"\nBuzz = {buzz_numbers}")
print(f"\nFizzBuzz = {fizz_buzz_numbers}")
print(f"\nNo Fizz or buzz = {no_fizz_buzz_numbers}")
clean()


#Excercise three
stop = int(input("Give me a stop number, where do you want stop; "))
stop_var = 0

if stop%2 == 0:
    stop_var = stop+1
even_numbers = []
sum_even_numbers = 0
for i in range(2,stop_var,2):
    sum_even_numbers+= i
    even_numbers.append(i)
print(f"The even numbers betwen 1 and {stop} are {even_numbers}")
print(f"The sum of, even numbers finded is {sum_even_numbers}")
clean()

#Excercint two
student_notes = input("Input a list of student notes: ").split()
for n in range(0, len(student_notes)):
  student_notes[n] = int(student_notes[n])
#Write your code below this row 
max_note= 0

for note in student_notes:
    if note > max_note:
        max_note = note

print(f"The highest score in the class is {max_note}")
clean()

#Excercise one
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
#Write your code below this row 

average = 0

for i in student_heights:
    average += i

lenght_list = 0
for i in student_heights:
    lenght_list+=1

average/=lenght_list
average = int(average)
print(f"The average of {lenght_list} students is {average}")
clean()
