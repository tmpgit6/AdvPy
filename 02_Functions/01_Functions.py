def greeting1():
    print("Hallo Mohamed")

def greeting2(name):
    print(f"Hallo {name}")

def greeting3(first_name, last_name):
    print(f"Hallo {first_name} {last_name}")

def greeting4(first_name, last_name, location = "Köln"):
    print(f"Hallo {first_name} {last_name} {location}")


greeting1()
greeting2("Thomas")
greeting3("Thomas", "Meier")
greeting3("Meier", "Thomas")

greeting3(last_name="Meier", first_name="Thomas")
greeting4("Sara", "Meier")
greeting4("Sara", "Meier", "AAchen")
