import os
c= lambda: os.system("clear")

#project in the end-day
def option_draw(n=0):
    
    if n ==0:
        print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
        ''')
    elif n==1:
        print("""
               ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO
       ::::::;       ;          OOOOO
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `#
        """)
    elif n==2:
        print("""
              __
                /__`.
               / \ `\\\\
              /   \  `\\
             /     \   \\
            /_______\  /\\
            (((( ))))
           (((' . ')))
           (((\_-_/)))
           (((_) (_)))
          /((( \ / )))\\
         / (((  ^  ))) \\
        / / ((  ^  )) \ \\
       ( (   \  ^  /   ) )
        \ \   )www(   / /
         `\\\\ /     \ //'
           /'       `\\
          /           \\
         /             \\
        /               \\
       /                 \\
      /                   \\
     /                     \\
    /                       \\
   /                         \\
  /                           \\ jgs
 |                             |
  `-----......_____......-----'
        """)


print("Welcome to Treasure Island.")
option_draw()
print("Your mission is to find the treasure.")

option_case = 0
option_input = input("left or right, press L or R?" ).lower()
if option_input == 'l':
    option_input = input("swim or wait?, S or W ").lower()
    if option_input == 'w':
        option_input = input("Wich door, RED,YELLOW or BLUE? R, Y or B ").lower()
        if option_input == 'r':
            c()
            option_draw(1)
            print("Burned by fire, \n\nGAME OVER!")
            input()
            c()
        elif option_input == 'y':
            c()
            option_draw(2)
            print("You win, \n\nBYE BYE!")
            input()
            c()
        else:
            c()
            option_draw(1)
            print("Eaten by beasts, \n\nGAME OVER!")
            input()
            c()
    else:
        c()
        print("Attacked by trout!\n\nGAME OVER!")
        option_draw(1)
        input()
        c()
else:
    c()
    print("Fall into a hole, \n\nGAME OVER!")
    option_draw(1)
    input()
    c()



#PRACTICE FIVE
"""
Take both people's names and check for the number of times the letters in 
the word TRUE occurs. Then check for the number of times the letters in the word LOVE
occurs. Then combine these numbers to make a 2 digit number. 
"""
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
names = name1 + name2

true_times_apear = names.count('t')
true_times_apear += names.count('r')
true_times_apear += names.count('u')
true_times_apear += names.count('e')

love_times_apear = names.count('l')
love_times_apear += names.count('o')
love_times_apear += names.count('v')
love_times_apear += names.count('e')

love_score = true_times_apear*10+love_times_apear
if love_score < 10 or love_score >90:
    print(f'Your score is {love_score}, you go together like coke and mentos')
elif love_score >=40 and love_score <= 50:
    print(f'Your score is {love_score}, you are alright together')
else:
    print(f'Your score is {love_score}')
input()
c()

#PRACTICE FOUR
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ").upper()
add_pepperoni = input("Do you want pepperoni? Y or N ").upper()
extra_cheese = input("Do you want extra cheese? Y or N ").upper()

price = 0
string = "" 

if size == 'S':
    price = 15
    string+= "Your small pizza, "
elif size == 'M': 
    price = 20
    string+= "Your medium pizza, "
else:
    price = 25
    string+= "Your large pizza, "

if add_pepperoni == 'Y':
    string+= "whit peperoni, "

    if size == 'S':
        price += 2
    else: price+=3
if extra_cheese == 'Y':
    string+= "whit cheese, "
    price+=1

print(string,"is cost ",price)
input()
c()


#ejercicio 1

print("Welcome to the rollcoaster")
height_1 = int(input("What is your height in cm? "))
age = int(input("What is your age in years? "))
if height_1 > 120:
    print("You can ride the rollercoaster!")
    if age<12:
        cost = 5
    elif age <= 18:
        cost = 7
    else:
        cost = 12
    photho = int(input("Press 1, if you want a phone, whatever is yo don't"))
    if int(photho) == 1:
        cost=cost+3
        print(f"Your ticket cost is {cost}$")
    else:
        print(f"Your ticket cost is {cost}$")
else:
    print("Sorry, you have to grow taller before you can ride.")
input()
c()




#practice three
year = int(input("Give me a year: "))

if year%4 ==0:
    if year%100==0:
        if year%400==0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is a normal year")
    else:
        print(f"{year} is a leap year")
else:
        print(f"{year} is a normal year")
input()
c()

#practice two
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

BMI = weight / height ** 2
BMI = round(BMI, 2)

if BMI<18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI<25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI<30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI<35:
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clinically obese.")
input()
c()


#practice one

#  Don't change the code below 
number = int(input("Which number do you want to check? "))
#  Don't change the code above 

#Write your code below this line 
if number%2 == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odder number")

input()
c()

