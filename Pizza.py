pizza = input("Which Size pizza you want ot buy?(Small/Large/Medium)")
bill = 0
if pizza == "small" or pizza == "Small":
    bill += 150
    print("Small Pizza price is 150 BDT.")
elif pizza == "medium" or pizza == "Medium":
    bill += 350
    print("Medium Pizza price is 350 BDT.")
else:
    bill += 550
    print("Large Pizza price is 550 BDT.")

add_pep = input("Do you want to add extra peperoni?(Y/N)")
if add_pep == "y" or add_pep == "Y":
    if pizza == "small" or pizza == "Small":
        bill += 50
    else:
        bill += 100
add_cheese = input("Do you want to add extra cheese?(Y/N)")
if add_cheese == "y" or add_cheese == "Y":
    bill += 50
print(f"Your total bill is {bill}.")
print("Enjoy Your meal.Happy Tummy *_*")
