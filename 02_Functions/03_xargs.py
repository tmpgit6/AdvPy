# *: beliebiger Anzahl von Arugments
def add(*xargs):
    print(sum(xargs))


add(10, 20)
add(10, 20, 30 )
add(10, 20, 30, 40 )