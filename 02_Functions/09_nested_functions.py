def greeting(name): # Outer Function
    print("Hallo")

    def bye(): # Inner Function
        print("Bye Bye", name)
    return bye

# Caller


result = greeting("Thomas")
print(result)

result() # Call the Inner Function

result2 = greeting("Sara")
result2()
result()
print()
########################

def add(x):
    
    def calc(y):
        print(x + y)

    return calc

calculator = add(10)
calculator(20)
######################
# Factory
def power_generator(num):
    def calc(power):
        print(num ** power )
    
    return calc 

power_of_two = power_generator(2)
power_of_two(3)

power_of_three = power_generator(3)
power_of_three(2)








