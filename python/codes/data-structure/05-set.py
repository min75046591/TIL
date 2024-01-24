my_set = {'a', 'b', 'c', 1, 2, 3}

my_set.add(4)
print(my_set)

my_set.add(4)
print(my_set)

my_set.remove('a')
print(my_set)

# my_set.remove('z')
# print(my_set)  # KeyError: 'z'

element = my_set.pop()
print(element)

my_set.update([1, 4, 5])
print(my_set)

my_set.discard(1)
print(my_set)

my_set.discard('z')
print(my_set)

# my_set = {'a', 'b', 'c', 'd'}
# element = my_set.pop()
# print(element)


# my_set.clear()
# print(my_set)

set1 = {0, 1, 2, 3, 4}
set2 = {1, 3, 5, 7, 9}
set3 = {0, 1}

print(set1.difference(set2))  # {0, 2, 4}
print(set1.intersection(set2))  # {1, 3}
print(set1.issubset(set2))  # False
print(set1.issuperset(set2)) # False
print(set1.issuperset(set3))  # True
print(set1.union(set2))  # {0, 1, 2, 3, 4, 5, 7, 9}