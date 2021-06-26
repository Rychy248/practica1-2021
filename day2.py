import os
c= lambda: os.system("clear")
###############LAST EXCERCICE
#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
bill = float(input("give me the bill, price: "))
people_number = int(input("Give the people number: "))
impuest = float(input("Give the porcent impuest: "))/100
each_person_cost = bill/people_number*(1+impuest)
print(f"Each person should pay {each_person_cost:.2f}") #2f it's show zeros no significatives 





###############EXCERCICE FOUR
#  Don't change the code below 
age = input("What is your current age? ")
#  Don't change the code above 
print("if you will live 90 years, the time you have left is...")
years = 90-int(age)
print(f"You have {years*365} days, {years*52} weeks, {years*12} months, {years} yearseleft.")
print("\n\n")
#Write your code below this line 

###############EXCERCICE THREE
#  Don't change the code below 
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
#  Don't change the code above 

#Write your code below this line 
height = float(height)
weight = float(weight)
print("Your body mass index is "+str(int(weight/height**2))+"! ")
print("-----------\n")
###############EXCERCICE TWO
print(3*3/3+3-3)



###############EXCERCICE ONE
two_digit_number = input("Type a two digit number: ")
####################################
#Write your code below this line 

result =0
two_digit_number = str(two_digit_number)
lenght = len(two_digit_number)

for l in range(lenght):
    result += int(two_digit_number[l])
string=""
for f in range(lenght):
    if f < (lenght-1):
        string += two_digit_number[f] + " + "
    else:
        string += two_digit_number[f]+" = "
print(string+str(result))
print("--------------------\n")
input()
c()
