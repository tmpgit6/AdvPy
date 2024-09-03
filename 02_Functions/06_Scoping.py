location = "Berlin"


def greeting(name):
    print(name, location)


def greeting2(name):
    location = "Aachen" # creates a NEW local variable
    print(name, location)

def greeting3(name):
    global location # makes the global variable writable
    location = "Frankfurt" # creates a NEW local variable
    print(name, location)


def greeting4():
    print("Hallo Mohamed")

def greeting4():
    print("Hallo Ingo")

def greeting4():
    print("Hallo Sara")

greeting("Thomas")
greeting2("Sven")
print(location) # Berlin


greeting3("Armin")
print(location) # Frankfurt


greeting4()