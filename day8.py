import os
import math
import random
import day8_art

c = lambda : os.system('clear')

def clean():
    input("\n\nPress enter, to continue....")
    c()

#PROYECT
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
        'v', 'w', 'x', 'y', 'z']

def encode(message,shift=1,direction=""):
    encrypted_message = ""
    alphabet_weigth = len(alphabet) -1

    if direction == "decode":
        shift*=-1

    for letter in message:
        if letter in alphabet:
            index_letter = alphabet.index(letter)
            index_encrypted_letter = index_letter+shift

            if direction == "decode":
                while index_encrypted_letter < 0:
                    index_encrypted_letter += alphabet_weigth
            else:
                while index_encrypted_letter > alphabet_weigth:
                    index_encrypted_letter-=alphabet_weigth

            encrypted_letter = alphabet[index_encrypted_letter]
            encrypted_message += encrypted_letter
        else:
            encrypted_message += letter

    print(f"The {direction}d messegue is:\n{encrypted_message}")
    print("\n\n")


option = 1
while option != 0:
    print(day8_art.logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    
    c()
    if direction == "encode" or direction == "decode":
        direction = direction.lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        
        encode(message=text,shift=shift,direction=direction)

    else:
        print("Invalid option")

    clean()
    option = int(input("Type 0 to break: "))

clean()




#E j e r c i c e   THREE
#pensar en que los compuestos cada vez que se duplican solo aumnetan en un divisor
#ese di isor es el numero compuesto anterior multilicado por dos

def prime_checker(number):
    divisors = [number]

    index = 1
    is_prime = "I don't know"

    while len(divisors) <= 2:
        if number == index:
            break
        elif (number % index) == 0:
            divisors.append(index)
        
        index+=1

    #print(f"Divisors finded = {divisors}\n")

    if len(divisors) ==2:
        is_prime = "prime"
    #    print("It's a prime number.")
    else:
        is_prime = "composed"
        #print("It's not a prime number.".upper().center(40))
    
    #print("\n")
    return is_prime

option = 1
while option != 0:
    until = int(input("Type a number where do you want to chek primes numbers: "))
    primes = []
    composeds = []
    until +=1

    for i in range (1,until):
        number_check = prime_checker(i)
        
        if i == 1:
            pass
        elif number_check == "prime":
            primes.append(i)
        else:
            composeds.append(i)

    print(f"Primes finded until {until-1} are: \n{primes}\n")
    watch_numbers = int(input("Do you want to see the composed numbers? 1 = yes, 0 = no; "))
    if watch_numbers == 1:
        print(f"Composeds finded until {until-1} are:\n{composeds}\n")

    clean()
    option = int(input("Type 0 to break: "))



clean()

#E j e r c i c e   TWO
#Write your code below this line 👇
def paint_calc(height,width,cover):
    area = height * width
    numbers_cans = math.ceil(area/cover)
    print(f"You'll need {numbers_cans} cans of paint")

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
clean()

#E j e r c i c e   ONE
#funtions

def greet(name,location):
    print(f'\nHello {name}')
    print(f'How do you do {name}? ')
    print(f'You are from {location}')
    print(f'Is not a greit day?')

greet(location=input("Where do you from? "),name=input("Your name is? "))


