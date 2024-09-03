my_list= ["Thomas", "Ingo", "Sara", "Lena"]
print(my_list)


# Add new items
my_list.append("Frank")
print(my_list)

my_list.insert(1, "Julia")
print(my_list)


# Change an Item
my_list[2] = "CAN"
print(my_list)

# Access Items
print(my_list[0])
print(my_list[1:100])
print(my_list[1:100])
print(my_list)  # ['Thomas', 'Julia', 'CAN', 'Sara', 'Lena', 'Frank']
print(my_list[-1: -4])
print(my_list[-3 : 0])
print(my_list[-3:])
print(my_list[-3:-1])

# Delete Items
my_list.pop()
print(my_list)

my_list.pop(1)
print(my_list)

my_list.remove("Sara")
print(my_list)


del my_list[0]
print(my_list)

del my_list[0:2]
print(my_list)

course = "Python"


my_list= ["Thomas", "Ingo", "Sara", "Lena"]
print(my_list[:])



