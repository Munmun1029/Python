Height = float(input("What is your height in ft?"))
Bill = 0
if Height >= 3:
    print("You can ride.")
    age = int(input("What is Your Age?"))
    if age < 12:
        Bill = 150
        print("Ticket price is 150 BDT.")
    elif age <= 18:
        Bill = 250
        print("Ticket price is 250 BDT.")
    else:
        Bill = 350
        print("Ticket price is 350 BDT.")
    photo = input("Do you wants to take Photos? press(Y/N)")
    if photo == 'y' or photo == 'Y':
        Bill = Bill+50
        print(f"Your Total bill is {Bill}")
    else:
        print(f"Your Total bill is {Bill}")

else:
    print("You can not ride.")
print("Thank You ! enjoy your day. ")

