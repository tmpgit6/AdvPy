numbers = [1,2,3,4,5]

# Physical List []
sqaured_list = [num * num for num in numbers]
print(sqaured_list)


# Generator ()
sqaured_list2 = (num * num for num in numbers)
print(sqaured_list2)

for num in sqaured_list2:
    print(num)