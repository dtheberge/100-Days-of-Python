# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

years_left = 90 - int(age)

months = years_left * 12 
days = years_left * 365
weeks = years_left * 52

#Write your code below this line 👇
print(f"You have {days} days, {weeks} weeks, and {months} months left.")