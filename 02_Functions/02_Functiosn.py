def add1(x, y):
    total = x + y 
    print("Total:", total)
    

def add2(x, y):
    total = x + y 
    return total 


def add3(x, y):
    total = x + y 
    return total, "Die Summe ist", True


add1(1,4)


result = add2(20, 30)
print(result)

# Unpacking
summe, nachricht, anwesend = add3(10,60)
print(summe, nachricht, anwesend)


container = add3(10,60)
print(container, type(container))