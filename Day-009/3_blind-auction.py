import art
from replit import clear
#HINT: You can call clear() to clear the output in the console.

print(art.logo)

again = 'y'
bidders = {}

while(again.lower() == 'y'):
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))
    bidders[name] = bid

    again = input("Is there another bidder? ")
    clear() # Done in Replit

highest_name = ""
highest_bid = 0

for bidder in bidders:
    if bidders[bidder] > highest_bid:
        highest_name = bidder
        highest_bid = bidders[bidder]

print(f"{highest_name} has the highest bid at ${highest_bid}")
