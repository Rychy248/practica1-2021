#CREATED BY RYCHY, contact me -> jorgeajrhh@gmail.com

import os
import time
import random
from day14_art import logo, vs
from day14_data import data


def c():
    if os.name in ['nt', 'dos']:
        command = "cls"
    else:
        command = "clear"
    os.system(command)


def clear():
    stay = input("Press enter to continue...")
    c()


def get_element(players=[], add=2):
    index_leght = len(data) - 1
    for i in range(0, add):
        rand_index = random.randint(0, index_leght)
        players.append(data[rand_index])
    return players


def show_options(players=[]):
    print(f"Compare A: {players[0]['name']}, a {players[0]['description']}, from {players[0]['country']}")
    print(vs)
    print(f"Againts B: {players[1]['name']}, a {players[1]['description']}, from {players[1]['country']}")


def compare(players, option):
    result = 0  # tie
    if players[0]['follower_count'] > players[1]['follower_count']:
        if option == 0:
            result = 1  # win A
        else:
            result = 2  # lose A
    elif players[0]['follower_count'] < players[1]['follower_count']:
        if option == 1:
            result = 1  # win B
        else:
            result = 2  # lose B
    return result


def main():
    def add_gamer(option_var):
        nonlocal gamers
        if option_var == 'a':
            gamers.pop(0)
        else:
            gamers.pop(1)
        gamers = get_element(gamers, 1)

    gamers = []
    score = 0
    gamers = get_element(gamers, 2)
    lose = False
    lives = 3
    while not lose:
        option = 'w'
        print(logo, f"\n<<<<<< S C O R E = {score} | L I V E S = {lives} >>>>>>")
        while option not in ['a', 'b']:
            show_options(gamers)
            option = input("Who has more followers? Type 'A' or 'B':")
            option = option.lower()
            if option not in ['a', 'b']:
                print("No valid option!\nTry Again!")
                time.sleep(1)
                c()
                print(logo, f"\n<<<<<< S C O R E = {score} | L I V E S = {lives} >>>>>>")
        if option == 'a':
            result = compare(gamers, option=0)
        else:
            result = compare(gamers, option=1)
        print(f"\n{gamers[0]['name']}, {gamers[0]['follower_count']}M, "
              f"{gamers[1]['name']}, {gamers[1]['follower_count']}M")
        if result == 0:
            print("Let's continue!")
            add_gamer(option)
            gamers = get_element(gamers, 1)
        elif result == 1:
            print("Wow, you got it, let's go on!")
            add_gamer(option)
            score += 1
        else:
            print("YOu lose :(, try again")
            lives -= 1
            print(f"\nYour score is {score}, lives = {lives}")
        if lives == 0:
            lose = True
        clear()


continue_game = True
while continue_game:
    main()
    try_again = input("Type 'yes' to continue or whatever if not: ")
    if try_again.lower() != 'yes':
        continue_game = False
