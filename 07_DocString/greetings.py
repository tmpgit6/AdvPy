__author__ = "Mohamed"
__version__ = 1.0
__doc__ = """This a module"""
__banana__ = "Apfel"
__responsible__ = "Ananas"
__license__ = ""


print(__name__)

LOCATION = "Berlin"

def greeting_de(name):
    print("Hallo", name)

def greeting_en(name):
    print("Hello", name)

def greeting_sp(name):
    print("Hola", name)


def greeting_tr(name):
    print("Merhaba", name)


def greeting_cn(name):
    print("Nihawo", name)

def greeting_fr(name):
    print("Salut", name)



if __name__ == "__main__":
    greeting_cn("Thomas")