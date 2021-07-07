import os
import day9_art as art

c = lambda : os.system('clear')

def clean():
    input("\n\nPress enter, to continue....")
    c()


#FINAL PROJECT
want_break = 0
clients = {}

while want_break != 1:
    print(art.logo)
    name = input("Type the name: ")
    bid = int(input("Type a bid: $"))
    clients[name] = bid
    
    other_user = input("\nIs there another client?, yes or no: ").lower()
    if other_user == "yes":
        c()
    else:
        winner = ""
        value = 0
        for client in clients:
            if clients[client] > value:
                winner = client
                value = clients[client]

        print(f"\n\nThe winer is {winner}, whit ${value}")
        clients = {}

        print("\n\n")
        want_break = int(input("Do you want to break loop, type 1? "))

clean()



#Ejercicio 1
def add_new_country(country,visits, cities):

    travel_log.append({
        "country":country,
        "visits":visits,
        "cities":cities

        })

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
#🚨 Do not change the code below


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

for i in travel_log:
    print(i)


clean()


#Ejercicio 0
student_scores = {
        "Maria":91,
        "Pedro":81,
        "Juan":71,
        "Marcos":70,
        "Lucia": 98,
        "Lucas": 88,
        "Martin": 78,
        "Gaby": 54,
}

student_grades = {}

for key,value in student_scores.items():
    if value >= 91:
        student_grades[key]="Outstanding"
    elif value >= 81:
        student_grades[key]="Exceeds Expectations"
    elif value >= 71:
        student_grades[key]="Acceptable"
    elif value <= 70:
        student_grades[key]="Fail"

print(student_grades)
