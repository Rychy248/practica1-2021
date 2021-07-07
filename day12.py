import os
import random

logo = """ 
  /$$$$$$                                         /$$                            /$$$$$$                                   
 /$$__  $$                                       |__/                           /$$__  $$                                  
| $$  \__/ /$$   /$$  /$$$$$$   /$$$$$$$ /$$$$$$$ /$$ /$$$$$$$   /$$$$$$       | $$  \__/  /$$$$$$  /$$$$$$/$$$$   /$$$$$$ 
| $$ /$$$$| $$  | $$ /$$__  $$ /$$_____//$$_____/| $$| $$__  $$ /$$__  $$      | $$ /$$$$ |____  $$| $$_  $$_  $$ /$$__  $$
| $$|_  $$| $$  | $$| $$$$$$$$|  $$$$$$|  $$$$$$ | $$| $$  \ $$| $$  \ $$      | $$|_  $$  /$$$$$$$| $$ \ $$ \ $$| $$$$$$$$
| $$  \ $$| $$  | $$| $$_____/ \____  $$\____  $$| $$| $$  | $$| $$  | $$      | $$  \ $$ /$$__  $$| $$ | $$ | $$| $$_____/
|  $$$$$$/|  $$$$$$/|  $$$$$$$ /$$$$$$$//$$$$$$$/| $$| $$  | $$|  $$$$$$$      |  $$$$$$/|  $$$$$$$| $$ | $$ | $$|  $$$$$$$
 \______/  \______/  \_______/|_______/|_______/ |__/|__/  |__/ \____  $$       \______/  \_______/|__/ |__/ |__/ \_______/
                                                                /$$  \ $$                                                  
                                                               |  $$$$$$/                                                  
                                                                \______/                                                   
""" 

c = lambda : os.system('clear')
def clean():
    """
    IT'S CLEAN YOUR CONSOLE
    """
    input("\n\nPress enter, to continue....")
    c()

#GLOAL VARIABLES
def hard():
    number = random.randint(1,101)
    attemps = 5
    return number, attemps

def easy():
    number = random.randint(1,51)
    attemps = 10
    return number, attemps

def verify(random_number,guess):
    c()
    print(logo)
    if random_number == guess:
        print("You got it!\n")
        print(random_number)
        play = False
    elif random_number < guess:
        print("Too high\nGuess agin!")
        play = True
    else:
        print("Too low\nGuess agin!")
        play = True
    return play 

def main():
    print(logo)
    print("""
Welcome to the Number Guessing Game!
I'm thtinking of a number between 1 and 100.
if you choose easy a number will be between 1 and 50.
if you choose hard a number will be between 1 and 100.
Choose a difficulty.
    """)
    user_option = ""
    while user_option not in ["easy","hard"]:
        user_option = input("Type 'easy' or 'hard': ")
        user_option = user_option.lower()
        if user_option not in ["easy","hard"]:
            print(f"{user_option} is'nt a valid option!")
            print("Try again!\n")

    levels = {
        "easy":easy,
        "hard":hard
    }
    level = levels[user_option]
    data = level() 
    random_number = data[0] 
    attemps = data[1]
    playin = True
    while playin:
        print(f"You have {attemps} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        playin = verify(random_number,guess) 
        attemps -= 1
        if attemps == 0:
            playin = False
    if attemps == 0:
        print(f"The number is {random_number}")
    clean()


main()
try_again = True

while try_again:
    option = input("Do you want try again?, yes or no ")
    if option == "yes":
        main()
    else:
        try_again = False

