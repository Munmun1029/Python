msg = input("Should I wait for you? ")
if msg == str("yes"):
    print("Okay, I Will wait.")
    ans = int(input("How long to wait?"))
    if ans < 30:
        print("I am waiting.")
    elif ans <= 60:
        print("Okay, Please come fast.")
    else:
        print("I am going to sleep.Good night.")
else:
    print("Okay,Good Night.Have a sweet dreams.")
