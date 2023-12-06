import random
print("************* Welcome To Complex Password Generator *************\n")

letters = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i',
           'J', 'j', 'K', 'k', 'L', ' l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q',
           'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['*', ' %', '#', '!', '/', '@', '$', '&', '(', ')', ';', ':', '|', '+', '=']

l_input = int(input("How many letters you want in your password?\n"))
s_input = int(input("How many symbols you want in your password?\n"))
n_input = int(input("How many numbers you want in your password?\n"))

complex_pass = []

for i in range(1, l_input+1):
    char = random.choice(letters)
    complex_pass += char
for i in range(1, s_input+1):
    char = random.choice(symbols)
    complex_pass += char
for i in range(1, n_input+1):
    char = random.choice(numbers)
    complex_pass += char

random.shuffle(complex_pass)
Password = ""
for char in complex_pass:
    Password += char
print(f"Your password is :{Password} ")
