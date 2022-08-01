#Write your code below this line 👇

def prime_checker(number):
    if(number < 0):
        number *= -1

    if(number > 1):
        for x in range(2, number):
            if (number % x == 0):
                return False

    return True

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))

if (prime_checker(number=n)):
    print("It's a prime number.")
else:
    print("It's not a prime number.")
