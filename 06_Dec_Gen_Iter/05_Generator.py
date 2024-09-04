# Classical Way without Generator
def square_number(numbers):
    squared_list = [] 
    for num in numbers:
        squared_list.append(num * num)

    return squared_list


sq_list = square_number( [1,2,3,4,5]  )
print(sq_list)


### With Generator

def square_gen(numbers):
    for num in numbers:
        yield num * num 

result_gen = square_gen([1,2,3,4,5])

print(result_gen)
for num in result_gen:
    print(num)

print(list(result_gen))