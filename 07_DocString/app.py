__author__ = "Mohamed"
__version__ = 1.0
__doc__ = """This a module"""


import greetings

print(__name__)
print(__file__)

def greeting(first_name:str, last_name:str, salary:int) -> float:
    """Greets the user and calculates the Brutt salary

    Args:
        first_name (str): First name of the employee
        last_name (str): Second name of the employee
        salary (int): the desired salary

    Returns:
        float: Salary with Brutt
    """
    print(first_name, last_name, salary)

    return salary * 1.07


def greeting2(name2:str) -> str:
    """_summary_

    Args:
        name2 (str): _description_

    Returns:
        str: _description_
    """
    
    try:
        num = 1 + 2
    except ValueError:
        print("Errror")

    return name2.strip()


greeting("Sara", "Meier", 50)

greeting("Meike","Meier", 5000)



# help(greeting)
help(greetings)

