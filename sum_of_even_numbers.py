total = 0
for i in range(1, 101):
    if i % 2 == 0:
        total += i
print(total)


# or

total = 0
for i in range(2,51,2):
    total += i
print(f"The sum is ={total}")
