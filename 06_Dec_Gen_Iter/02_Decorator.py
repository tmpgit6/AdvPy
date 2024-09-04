def logger(func):
    def wrapper(*args,**kwargs):
        print(f"Before the function {args} , {kwargs}")
        result = func(*args)
        print("After the function")
        return result
    return wrapper


@logger
def add(num1, num2):
    return num1 + num2 

@logger
def minus(num1, num2):
    return num1 - num2 


print(add(3,5))
print(minus(3,5))