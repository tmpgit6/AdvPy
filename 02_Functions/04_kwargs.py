# **: Dictionary (key, value)

def greeting(**kwargs): 
    print(kwargs) 
    for item in kwargs.items():
        print(item)


greeting(car = "VW", bj = 2020)

greeting(first_name = "Thomas", last_name = "Meier")