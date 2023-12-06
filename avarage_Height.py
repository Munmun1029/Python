height = input("Input all the heights separated by comma : ")

height_list = height.split(",")
count = 0
for height in height_list:
    count = count+1
print(count)
for i in range(count):
    height_list[i] = int(height_list[i])
Total = 0
for person in height_list:
    Total += person
avg = Total/count
print("The Average height is : " , round(avg))
