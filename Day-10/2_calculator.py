import art
from replit import clear


def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    return num_1 / num_2

def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def calculator():
    clear()
    new = "y"
    ans = -1

    print(art.logo)
    new_in = float(input("What is the first number?: "))

    while True:
        if new == "n":
            print(art.logo)
            new_in = float(input("What is the first number?: "))
            
        operation = input("Pick an operation?: \n+\n-\n*\n/\nYour Choice: ")
        num_2 = float(input("What is the second number?: "))

        if operation == "+":
            ans = add(new_in, num_2)
        elif operation == "-":
            ans = subtract(new_in, num_2)
        elif operation == "*":
            ans = multiply(new_in, num_2)
        else:
            ans = divide(new_in, num_2)

        print(f"{new_in} {operation} {num_2} = {ans}")
        if input(f"Type 'Y' if you want to continue with {ans}, or 'N' to start a new calculation: ").lower() == 'y':
            new_in = ans
        else:
            calculator()

calculator()