#CREATED BY RYCHY, contact me -> jorgeajrhh@gmail.com

import os
import random
import day7_art
import day7_words

c = lambda : os.system('clear')

def clean():
    input("\n\nPress enter, to continue....")
    c()

#Ejercicio ONE
#Step 1
def find_letter(chosen_word,guess,blanks):
    matches = []
    not_found = False
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            blanks[position]=letter
            matches.append(position)
    
    if len(matches) == 0:
        not_found = True
    return [blanks,not_found] 


def try_letters():
    word_list = day7_words.word_list 
    chosen_word = word_list[random.randint(0,(len(word_list)-1))]

    blanks = []
    for i in range(len(chosen_word)):
        blanks.append("_")

    stages = day7_art.stages
    
    letters_typed = []
    game_over = False
    lifes = 6
    win_or_lose = "lose"
    messegue = ""

    while not game_over:
        c()
        #its join, its a string, methos who can build a string from a iterable object
        # the string before de metod, will the string among the elements
        print(messegue)
        str_var = " ".join(blanks)
        print(stages[lifes])
        print(f"\n{str_var}\t\tL I F E S = {lifes}")
        guess = input("Input a letter: ").lower()

        check = find_letter(chosen_word,guess,blanks)
        not_matches = check[1]

        if not_matches == True:
            messegue = f"The ''{guess.upper()}'' isn't a valid letter, you losed a life!"
            lifes -= 1
        else:
            if guess in letters_typed:
                messegue = f"The ''{guess.upper()}'' was typed!"
            else:
                messegue = f"''{guess.upper()}'' is a valid letter!"
                blanks = check[0]
                letters_typed.append(guess)
     
        if "_" not in blanks:
            c()
            print(stages[lifes])
            str_var = (" ".join(blanks)).upper()
            print("_"*len(str_var)*2)
            print(f"| {str_var} |".center(len(str_var*2)))
            print("_"*len(str_var)*2)
            game_over = True
            win_or_lose = "win"
        if lifes ==0:
            c()
            print(stages[lifes])
            print(f"\n{str_var}\t\tL I F E S = {lifes}")
            game_over = True
            win_or_lose = "lose"


    if win_or_lose == "win":
        print("\n")
        print("C O N G R A T U L A T I O N S".center(32))
        print("Y O U    W I N".center(32))
    else:
        print("\n\nG A M E    O V E R")
        print("You Lose! :( \n\nTry again!")

    clean()


while True:
    print(day7_art.logo)
    print("Welcome to Hangman Game")
    exit = int(input("type 0 for exit "))
    if exit == 0:
        break
    else:
        try_letters()






