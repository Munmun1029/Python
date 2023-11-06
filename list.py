number = [1, 2, 3, 4, 5, 6]
name = ['mun', 'abir', 'mahi', 'shimu']
print(len(name))
print(name[1])

# [LENGTH]
print(name[0::2])

# sort list
name.sort()
print(name)

# reverse list

number.reverse()
print(number)

# insert list

name.insert(2, 'munni')
print(name)

# extend list

number.extend([7, 8, 9, 10])
print(number)

# change the list
name[2] = "Asad"
print(name)

# remove from list
name.remove("shimu")
print(name)

# remove the last element
number.pop()
print(number)

# count the list
print(name.count("mun"))


