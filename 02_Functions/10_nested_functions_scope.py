location = "Berlin"


def greeting(name):
    
    house_nr = 6
    print("Hallo", name)
    
    def bye():
        nonlocal house_nr
        house_nr += 1
         
        print("bye bye", name , location, house_nr)


    return bye 


result = greeting("Thomas")

result = greeting("Sara")
result()