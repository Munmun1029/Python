set1 = {"me", "you", "our", 29, 10, 16, 9}
set2 = {30, 6, 11, 7, "me", "you"}
print(set1)
# add something from set
set1.add(27)
print(set1)

# remove/ delete something from set
set1.remove(27)
print(set1)
print(len(set1))

# to remove random item from set
print(set1.pop())
print(set1)

# update
set1.update(['mun', 'mahi'])
print(set1)

# intersection
print(set1.intersection(set2))
print(set1 & set2)
# union
print(set1.union(set2))
# difference set1-set2
print(set1.difference(set2))
print(set1.symmetric_difference(set2))

# disjoint set
print(set1.isdisjoint(set2))

# subset
print(set1.issubset(set2))
print(set2 <= set1)

# superset
print(set1.issuperset(set2))
print(set2 >= set1)


