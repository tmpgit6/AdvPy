# many Form
# Polymorphism
class VSCode:
    def execute(self):
        print("I am a VSCODE IDE")

        
class PyCharm:
    def execute(self):
        print("I am a PyCharm IDE")

class Laptop:

    def run(self, ide):
        ide.execute()

my_ide1 = VSCode()
my_ide2 = PyCharm()


laptop1 = Laptop()

laptop1.run(my_ide1)
laptop1.run(my_ide2)

#############################################
# Method Overriding
class A:
    def show_me(self):
        print("I am A")

class B(A):

    def show_me(self):
        print("I am B")


b1 = B() 
b1.show_me()
