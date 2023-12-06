count = 5
while count <= 10:
    print(count)
    count += 2

else:
    print("count is printed")

game = int(input("Input a number (0 for quit the loop)"))
while game != 0:
    print(game)
    game = int(input("Input a number (0 for quit the loop)"))
else:
    print("You exit from the loop")
