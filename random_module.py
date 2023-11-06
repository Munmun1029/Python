import random
a = random.randint(1, 5)
b = random.randrange(1, 5)
c = random.random()
d = random.uniform(1, 5)

l = ['mun', 'abir',  2, 3, 'shimu', 5, 'mahi', 7]
e = random.choice(l)
random.shuffle(l)

print(a)
print(b)
print(c)
print(d)
print(e)
print(l)
