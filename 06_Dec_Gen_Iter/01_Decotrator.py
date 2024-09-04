def say_hello():
    print("Hello Mohamed")

def say_bye():
    print("Bye Mohamed")


def decorator(func):
    def wrapper():
        print("Before the function")
        func()
        print("After the function")
    return wrapper


result1 = decorator( say_hello )
result1()


result2 = decorator(say_bye)
result2()