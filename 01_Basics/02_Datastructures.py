my_tuple = (1, 2, "Python", True, [])


print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])


print(my_tuple)
my_tuple[4].append("AAA")
print(my_tuple)


# Work arround

tmp = list(my_tuple)
print(tmp)
tmp.append("Mohamed")
print(tmp)

my_tuple = tuple(tmp)

print(my_tuple)
