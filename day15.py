import os

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

def option():
    pass

def ask_coins():
    try_again = True
    while try_again:
        try:
            print('Please insert coins.')
            quarters = int(input('how many quarters?: '))
            dimes = int(input('how many dimes?: '))
            nickles = int(input('how many nickles?: '))
            pennies= int(input('how many pennies?: '))
            coins = quarters * 25 + dimes * 10 + nickles * 5 + pennies
            coins = round(coins/100,2)
            try_again = False
        except:
            print('Something was wrong!, Try again')

    return coins


def enough_money(coins_inserted,kind_coffe_selected):
    coins_var = 0
    bool_to_return = False

    if kind_coffe_selected == 'espresso': 
        coins_var = 1.25
    elif kind_coffe_selected == 'latte':
        coins_var = 1.50
    elif kind_coffe_selected == 'cappuchino':
        coins_var = 1.75
    if coins_var <= coins_inserted:
        bool_to_return = True

    return {'enough?':bool_to_return,'coffe_praice':coins_var}

def ask_resources(resources_stock,kind_coffe_selected):
    messegue = "Sorry there's not enough:"
    enough = True
    k_c_s = kind_coffe_selected
    resources_need = { 
        'espresso': {
            'Water': 30, #ml
            'Milk': 0, #ml
            'Coffee': 15 #g
            },
        'latte' : {
            'Water': 30, #ml
            'Milk': 10, #ml
            'Coffee': 10 #g
            },
        'cappuchino' : {
            'Water': 30, #ml
            'Milk': 15, #ml
            'Coffee': 10 #g
            }
        }

    if resources_stock['Water'] < resources_need[k_c_s]['Water']:
        messegue += " water, "
        enough = False
    if resources_stock['Milk'] < resources_need[k_c_s]['Milk']:
        messegue += " Milk, "
        enough = False
    if resources_stock['Coffee'] < resources_need[k_c_s]['Coffee']:
        messegue += "Coffe!"
        enough = False
    if enough:
        for key_element,element in resources_need[k_c_s].items():
            resources_stock[key_element] -= element 

    return {'enough?': enough,'messegue': messegue,'new_stock':resources_stock} 

def ingredients_report():
    resources_need = { 
        'espresso': {
            'Water': 30, #ml
            'Milk': 0, #ml
            'Coffee': 15 #g
            },
        'latte' : {
            'Water': 30, #ml
            'Milk': 10, #ml
            'Coffee': 10 #g
            },
        'cappuchino' : {
            'Water': 30, #ml
            'Milk': 15, #ml
            'Coffee': 10 #g
            }
        }

    for coffe_key,coffe_requeriments in resources_need.items():
        print("\n",coffe_key)
        for key,value in coffe_requeriments.items():
            print(f"{key} = {value}")


def report(stock):
    for key,value in stock.items():
        print(f"{key} = {value}")

def main():
    turn_off_machine = False
    stock = {
        'Water': 300, #ml
        'Milk': 200, #ml
        'Coffee': 100, #g
        'Money': 0 #$
    }

    while not turn_off_machine:
        coins = 0.0 #dollars
        selection = ""
        while selection not in ['espresso','latte','cappuchino','off','report','requeriments']:
            selection = input('What would you like? (espresso/latte/cappuchino): ')
            selection = selection.lower()
            if selection not in ['espresso','latte','cappuchino','off','report','requeriments']:
                print('\nInvalid Option!')
                clear()

        if selection in ['espresso','latte','cappuchino']:
            coins = ask_coins()
            money_test = enough_money(coins,selection)
            if money_test['enough?']:
                enough_resources = ask_resources(stock,selection) 
                if enough_resources['enough?']:
                    stock = enough_resources['new_stock'] 
                    stock['Money'] += money_test['coffe_praice'] 
                    if money_test['coffe_praice'] < coins:
                        print('\nHere is $',coins - money_test['coffe_praice']," in change.")
                    print(f"\nHere is your {selection} enjoy it!")
                else:
                    print(enough_resources['messegue'])
            else:
                print("Sorry that's not enough money, money refunded $",coins)
        elif selection == 'off':
            turn_off_machine = True
        elif selection == 'requeriments':
            ingredients_report()
        elif selection == 'report':
            report(stock)
        clear()


main()
