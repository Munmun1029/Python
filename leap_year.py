Year = int(input("Which year you wants to check? "))

if Year % 4 == 0:
    if Year % 100 == 0:
        if Year % 400 == 0:
            print("It is Leap Year.")
        else:
            print("It is not Leap Year.")
    else:
        print("It is Leap Year.")
else:
    print("It is not Leap year.")
