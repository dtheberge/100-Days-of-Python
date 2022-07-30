import resources

def check_resources(drink):
    sufficient = True

    if (not drink == 'espresso'):
        if(resources.MENU[drink]['ingredients']['milk'] > resources.resources['milk']):
            sufficient = False
            print("Sorry there is not enough milk.")
    
    if(resources.MENU[drink]['ingredients']['water'] > resources.resources['water']):
        sufficient = False
        print("Sorry there is not enough water.")
    
    if(resources.MENU[drink]['ingredients']['coffee'] > resources.resources['coffee']):
        sufficient = False
        print("Sorry there is not enough coffee.")

    return sufficient


def report():
    print(f"\nWater: {resources.resources['water']} ")
    print(f"Milk: {resources.resources['milk']}")
    print(f"Coffee: {resources.resources['coffee']}")
    print(f"Money: ${resources.resources['money']}")


def payment(drink):
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    total = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    if(resources.MENU[drink]['cost'] <= total):
        deduct_resources(drink)
        print(f"Thank you! Your change is ${round(total - resources.MENU[drink]['cost'], 2)}")
        print("Here is your latte. Enjoy!")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def deduct_resources(drink):
    if (not drink == 'espresso'):
        resources.resources['milk'] -= resources.MENU[drink]['ingredients']['milk']

    resources.resources['water'] -= resources.MENU[drink]['ingredients']['water']
    resources.resources['coffee'] -= resources.MENU[drink]['ingredients']['coffee']

def command():
    resources.resources['money'] = 0
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if(choice == 'off'):
        print("Powering Off.")
        exit()
    elif(choice == 'report'):
        report()
    elif(choice == 'espresso' or choice == 'latte' or choice == 'cappucino'):
        if (check_resources(choice)):
            if payment(choice):
                resources.resources['money'] += resources.MENU[choice]['cost']
    command()
    
command()