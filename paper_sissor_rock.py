import os
import random
c= lambda: os.system("cls")

def option_draw(n=0): 
    rock = '''
    R O C K
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

    paper = '''
    P A P E R
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

    scissors = '''
    S C I S S O R S
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

    if n ==0:
        print(rock)
    elif n==1:
        print(scissors)
    else:
        print(paper)
while True:
    break_option = int(input("input 0 to break: "))
    if break_option == 0:
        break
    c()

    player_option = int(input("input, 0 for rock, 1 for scissors, 2 for paper: "))
    machine_option = random.randint(0,2)
    if player_option > 2:
        player_option = 2
    if player_option < 0:
        player_option = 1

    print("Your option is ")
    option_draw(player_option)
    print("Machine option is ")
    option_draw(machine_option)


    if player_option == machine_option:
        print("Your and Machine, are TIES,\nLET'S TRY AGAIN!")
    elif player_option == 0 and machine_option == 2:
        print("Sorry you lose")
    elif player_option == 1 and machine_option == 0:
        print("Sorry you lose")
    elif player_option == 2 and machine_option == 1:
        print("Sorry you lose")
    else:
        print("Congratulations, YOU WIN!")
    input("\npress enter to continue... ")
    c()

print("\n") 
input("press enter to continue... ")
c()
