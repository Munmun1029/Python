import random

name = input("Enter everybody's names separated by space : ")
name_list = name.split(" ")

#print(name_list)
length = len(name_list)
random_choice = random.randint(0, length-1)
print(f"{name_list[random_choice]} will pay the bill .. ")


