name = input("What is your name?")
age = input("How old are you?")
height = input("How much taller you have?")
print(f"Your name is {name}.You are {age} years old.Your Height is {height} meters.")

Assignment = int(input("What is the last date of submission?"))

years_left = 1 - Assignment
month_left = years_left * 12
weeks_left = month_left * 4.2
days_left = month_left * 30
print(f"You have left {month_left} months, {weeks_left}weeks, {days_left}days.")