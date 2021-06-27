import os
import day10_art as art

c = lambda : os.system('clear')

def clean():
    input("\n\nPress enter, to continue....")
    c()


#DAY END PROJECT
def multiply(a,b):
    return a * b

def suma(a,b):
    return a + b

def rest(a,b):
    return a - b

def divide(a,b):
    return a / b
def exponentiation(a,b):
    return a ** b

def operation(operations={}):
    list_symbols = []

    invalid_operator = True
    while invalid_operator == True:
        for key_symbol in operations:
            list_symbols.append(key_symbol)
            print(key_symbol)
        operator = input("Pick an operation: ")

        if operator in list_symbols:
            invalid_operator = False
        else:
            print(f"\n'{operator}' isn't a invalid option!\n")

    return operator

def calculater(before_result=None):
    first_num = 0
    second_num = 0
    result = 0

    if before_result != None:
        first_num = before_result
    else:
        first_num = float(input("What's the first number? "))

    operations = {
            '+' : suma,
            '-' : rest,
            '*' : multiply,
            '/' : divide,
            '**' : exponentiation
    }

    operator = operation(operations)
    second_num = float(input("What's the next number? "))

    function = operations[operator]
    result = function(first_num,second_num)

    return [first_num,operator,second_num,result]

option = 1
while option != 0:

    print(art.logo)
    save = 'y'
    result = None
    
    while save == 'y':
        if result == None:
            #reset calculater
            result = calculater()
        else:
            #use before result
            result = calculater(result)
        # result = [first_number,operator, second_number,result]
        
        print(f"{result[0]} {result[1]} {result[2]} = {result[3]}")
        print("")
        save = input(f"Type 'y', to continue calculating with {result[3]}, or type 'n' to start a new calculation: ")
        save = save.lower()

        if save == 'y':
            result = result[3] #saving before result
        elif save=='n':
            result = None #deleting before result
            c()
        else:
            print("\nInvalid option, interpreted as 'n'")
            save = 'n'
            result = None #deleting before result
            c()

    option = int(input("\nDo you want exit, yes = 0?"))

clean()


#EJercicio two
def print_month(year,month_index,days):
    month_names = ["january","February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"]
    
    calendar = f"--- [{year}] [{month_names[month_index]}] ---\n".center(42)

    day = 1
    while day <= days:
        calendar_line = ""
        column = 0

        while day <= days and column < 7:
            calendar_line+= f"[{day}]".center(4) 
            column +=1
            day+=1
        calendar+= calendar_line+"\n"

    return calendar


def is_leap(year):
    is_leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                is_leap = True
            else:
                is_leap = False
        else:
            is_leap = True
    else:
        is_leap = False

    return is_leap



def days_in_month(year,month):
    year_leap_or = is_leap(year)

    days = 0
    month_index = month -1 

    if year_leap_or == False:
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
        days = month_days[month_index]
    else:
        month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
        days = month_days[month_index]

    calendar = print_month(year,month_index,days)
    return calendar 


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)

print(days)
clean()


#EJercicio one

def format_name(f_name, l_name):
    
    f_name = f_name.title()
    l_name = l_name.title()

    return f"{f_name} {l_name}"

print(format_name('RYchy','Hernández'))

clean()





