class Employee:

    def __init__(self, first_name, last_name) :
        self.first_name = first_name
        self.last_name = last_name 
  
    @classmethod
    def create_from_one_string(cls,name) :
        first_name, last_name = name.split(" ")
        last_name = last_name.upper()

        return cls(first_name, last_name)
    
    @classmethod
    def create_from_dashed_string(cls,name) :
        first_name, last_name = name.split("-")
        last_name = last_name.upper()

        return cls(first_name, last_name)

    

    def __repr__(self) -> str:
        return f"{self.first_name} - {self.last_name}"


# Consumer
thomas = Employee("Thomas", "Meier")
ingo = Employee("Ingo", "Meier")

sara = Employee.create_from_one_string("Sara Meier")
julia = Employee.create_from_dashed_string("Julia-Meier")

print(thomas)
print(sara)
print(julia)




