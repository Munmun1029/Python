import random

my_choice = int(input("Enter your choice : \n 0 for Rock \n 1 for Paper \n 2 for Scissor \n "))
if my_choice >= 3 or my_choice < 0:
    print("Invalid Number, Computer Win!!!")
else:
    computer_choice = random.randint(0, 2)
    print(' Computer Choose: ')
    print("", computer_choice)
    if computer_choice == my_choice:
        print(" It's DRAW 😝 ")
    elif computer_choice == 0 and my_choice == 2:
        print(" Computer Win!!!")
    elif my_choice == 0 and computer_choice == 2:
        print(" You Win !!!")
    elif computer_choice > my_choice:
        print(" Computer Win!!!")
    elif my_choice > computer_choice:
        print(" You Win!!!")
