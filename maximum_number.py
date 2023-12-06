numbers = input("Write you numbers which is separated by comma. ")

number_list = numbers.split(",")
count = 0

for i in number_list:
    count = count + 1
print(f"The length of the list is:{count}")
for i in range(count):
    number_list[i] = int(number_list[i])

max_number = number_list[0]
for i  in  number_list:
    if i > max_number:
        max_number = i
print(f"The maximum number is : {max_number}")
