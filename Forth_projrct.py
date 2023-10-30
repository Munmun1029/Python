# type casting int() , str(), float()
name = input("What is your name?")
length = len(name)
print("Your name length is " + str(length) + " character")


F_number = input("Enter your first number : ")
S_number = input("Enter Your Second number : ")

Sum = int(F_number) * int(S_number)
print("Answer : " + str(Sum))

number = input("Enter your two digits Number: ")
F_digit = number[0]
S_digit = number[1]
print(int(F_digit)+int(S_digit))
