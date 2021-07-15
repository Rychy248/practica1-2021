#CREATED BY RYCHY, contact me -> jorgeajrhh@gmail.com

import os
import random
c= lambda: os.system("clear")


#project in the end-day
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

#EXCERCICE THREE
# 🚨 Don't change the code below 👇
row1 = ["[]","[]","[]"]
row2 = ["[]","[]","[]"]
row3 = ["[]","[]","[]"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆
#Write your code below this row 👇
y_position = int(position[0])-1
x_position = int(position[1])-1
if y_position > 2:
    y_position = 2
if x_position > 2:
    x_position = 2

map[y_position][x_position] = "x "

print(f"{map[0]}\n{map[1]}\n{map[2]}")
input("press enter to continue... ")
c()



#EXCERCICE TWO
names = ['Nobody']
i = 0
while True:
    option = int(input("Press 0 to exit, or 1 to insert names: "))
    name = ""
    if option == 0:
        break
    else:
        name = input("Type the name: ")
    if i==0:
        names[0] = name
        i+=1
    else:
        names.append(name)
random_name = random.choice(names)
print(random_name," is going to buy the meal today!")
input("press enter to continue... ")
c()
print("\n\n")

#EXCERCICE ONE
for i in range(8):
    show_option = random.randint(0,1)
    if show_option == 0:
        messegue = "Tails".capitalize()
    else:
        messegue = "Heads".capitalize()
    print(messegue,"    ",end="")
    
input()
c()
print("\n\n")
