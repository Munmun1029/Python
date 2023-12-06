tuple1 = (29, 10, "mun", True, 27, 29)
tuple2 = (7, 45, 30, False)


# separated  tuple
tuple3 = (tuple1, tuple2)

# marge
tuple4 = tuple1 + tuple2
print(tuple3)
print(tuple4)
print(len(tuple3))
print(len(tuple4))

# counting
print(tuple1.count(29))

# index checking number

print(tuple1.index(29))

