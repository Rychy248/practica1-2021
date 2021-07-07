from day16_menu import Menu, MenuItem
from day16_coffee_maker import CoffeeMaker
from day16_money_machine import MoneyMachine
from clean import c, clear

class CoffeeMachine:
    def __init__(self):
        self.menu = Menu()
        self.money_machine = MoneyMachine()
        self.coffe_maker = CoffeeMaker()

    def turn_off(self):
        """Turn off the machine"""
        c()
        print("Sleep...")

    def serv_options(self):
        """Show the coffees it can make"""    
        valid_option = False
        instrucction = ""
        while not valid_option:
            instrucction = input('What would you like? (espresso/latte/cappuccino: ').lower()
            if instrucction not in ['espresso','latte','cappuccino','off','report']:
                print('\nInvalid Option!')
                clear()
            else:
                valid_option = True
        if instrucction in ['espresso','latte','cappuccino']:
            drink_ordered = self.menu.find_drink(instrucction)   
            if self.coffe_maker.is_resource_sufficient(drink_ordered):
                if self.money_machine.make_payment(drink_ordered.cost):
                    self.coffe_maker.make_coffee(drink_ordered)
            clear()
            self.serv_options()
        elif instrucction == 'off':
            self.turn_off()
        elif instrucction == 'report':
            self.coffe_maker.report()
            self.money_machine.report()
            clear()
            self.serv_options()

coffie_machine = CoffeeMachine()
coffie_machine.serv_options()
