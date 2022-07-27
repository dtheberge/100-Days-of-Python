#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""
for n in range(0, nr_letters):
    letter = letters[random.randint(0, len(letters) - 1)]
    password = password + letter

for n in range(0, nr_symbols):
    symbol = symbols[random.randint(0, len(symbols) - 1)]
    password = password + symbol

for n in range(0, nr_numbers):
    number = numbers[random.randint(0, len(numbers) - 1)]
    password = password + number

print("Your password is " + password + "\n\n")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = list(password)
randomized = []

while (password):
    pulled = random.randint(0, len(password) - 1)
    randomized.append(password[pulled])
    password.pop(pulled)

print("Your password randomized is " + "".join(randomized))