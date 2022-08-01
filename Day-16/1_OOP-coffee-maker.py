from decimal import MIN_ETINY
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

### Bug - The Resources don't update when a drink is made

def command():
    menu = Menu()
    coffeeMaker = CoffeeMaker()
    moneyMachine = MoneyMachine()

    choice = input(f"\nWhat would you like? ({menu.get_items()}): ")
    
    if(choice == 'off'):
        print("\nPowering Off.")
        exit()

    elif(choice == 'report'):
        coffeeMaker.report()

    elif(choice in ['espresso', 'latte', 'cappucino']):

        drink = menu.find_drink(choice)
        if(coffeeMaker.is_resource_sufficient(drink) and moneyMachine.make_payment(drink.cost)):
            coffeeMaker.make_coffee(drink)

    command()
    
command()
