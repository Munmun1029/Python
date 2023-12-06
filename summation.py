total = 0
number = int(input("Enter your numbers (0 for sum):"))
while number != 0:
    total += number
    number = int(input("Enter your numbers (0 for sum):"))
print("The sum is =", total)
